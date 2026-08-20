# -*- coding: utf-8 -*-
"""Независимое воспроизведение стратегий paulcpk/freqtrade-strategies-that-work.

ЗАЧЕМ. Автор публикует таблицу результатов, но НЕ публикует конфигурацию,
которая их породила (в репозитории 0 json-файлов, minimal_roi закомментирован
во всех пяти файлах). Прежде чем что-либо утверждать об устойчивости, надо
проверить ВОСПРОИЗВОДИТСЯ ЛИ заявленное число вообще.

Модель исполнения — как в freqtrade: сигнал на свече i исполняется по
ОТКРЫТИЮ свечи i+1. Стоп и трейлинг проверяются внутри свечи по low.
Одна открытая сделка на пару.

Индикаторы повторяют TA-Lib: EMA засевается SMA на первых `period` барах,
RSI — сглаживание Уайлдера. Это важно: pandas.ewm по умолчанию засевает
иначе, и на коротких периодах расхождение заметно.
"""
import os, sys, math
import pandas as pd, numpy as np

DATA = "./data"
PAIRS = ["BTCUSDT","LTCUSDT","ETHUSDT","XRPUSDT","ADAUSDT","XLMUSDT","XMRUSDT","DASHUSDT"]
IN_S, IN_E = "2018-03-01", "2020-03-01"

def ema(s, n):
    out = np.full(len(s), np.nan)
    if len(s) < n: return pd.Series(out, index=s.index)
    a = 2.0/(n+1.0)
    v = s.iloc[:n].mean(); out[n-1] = v
    arr = s.values
    for i in range(n, len(s)):
        v = (arr[i]-v)*a + v; out[i] = v
    return pd.Series(out, index=s.index)

def rsi(s, n):
    d = s.diff(); up = d.clip(lower=0); dn = -d.clip(upper=0)
    out = np.full(len(s), np.nan)
    if len(s) <= n: return pd.Series(out, index=s.index)
    au = up.iloc[1:n+1].mean(); ad = dn.iloc[1:n+1].mean()
    out[n] = 100.0 if ad == 0 else 100 - 100/(1+au/ad)
    u = up.values; w = dn.values
    for i in range(n+1, len(s)):
        au = (au*(n-1)+u[i])/n; ad = (ad*(n-1)+w[i])/n
        out[i] = 100.0 if ad == 0 else 100 - 100/(1+au/ad)
    return pd.Series(out, index=s.index)

def crossed_above(a, b):
    return (a > b) & (a.shift(1) <= b.shift(1))
def crossed_below(a, b):
    return (a < b) & (a.shift(1) >= b.shift(1))

# ── стратегии: (индикаторы, buy, sell, стоп, трейлинг) ──────────────
def s_double_ema(df):
    df["ema9"]=ema(df.close,9); df["ema21"]=ema(df.close,21); df["ema200"]=ema(df.close,200)
    buy = crossed_above(df.ema9,df.ema21) & (df.low>df.ema200) & (df.volume>0)
    sell= crossed_below(df.ema9,df.ema21) | (df.low<df.ema200)
    return buy, sell, 0.20, False

def s_macd(df):
    e12=ema(df.close,12); e26=ema(df.close,26)
    macd=e12-e26; sig=ema(macd.dropna(),9).reindex(df.index)
    df["macd"]=macd; df["sig"]=sig; df["ema100"]=ema(df.close,100)
    buy = (df.macd<0) & crossed_above(df.macd,df.sig) & (df.low>df.ema100) & (df.volume>0)
    sell= crossed_below(df.macd, pd.Series(0.0,index=df.index)) | (df.low<df.ema100)
    return buy, sell, 0.20, False

def s_rsi_fast(df):
    df["rsi"]=rsi(df.close,4); df["ema100"]=ema(df.close,100)
    k15=pd.Series(15.0,index=df.index); k85=pd.Series(85.0,index=df.index)
    buy = crossed_above(df.rsi,k15) & (df.low>df.ema100) & (df.volume>0)
    sell= crossed_above(df.rsi,k85) | (df.low<df.ema100)
    return buy, sell, 0.10, True

def s_rsi_slow(df):
    # ПОПРАВКА 20.08: пороги подставлялись по аналогии с быстрой RSI (15/85).
    # В файле они ДРУГИЕ: вход crossed_above(rsi,25), выход crossed_below(rsi,20).
    # Ошибка дала 18 сделок вместо сотни и едва не уехала в публикацию.
    df["rsi"]=rsi(df.close,10); df["ema600"]=ema(df.close,600)
    k25=pd.Series(25.0,index=df.index); k20=pd.Series(20.0,index=df.index)
    buy = crossed_above(df.rsi,k25) & (df.low>df.ema600) & (df.volume>0)
    sell= crossed_below(df.rsi,k20) | (df.low<df.ema600)
    return buy, sell, 0.20, True

def s_ema800(df):
    df["ema800"]=ema(df.close,800); df["thr"]=df.ema800*0.99
    buy = crossed_above(df.close,df.ema800) & (df.volume>0)
    sell= crossed_below(df.close,df.thr)
    return buy, sell, 0.15, True

STRATS = {
 "DoubleEMACrossoverWithTrend": s_double_ema,
 "MACDCrossoverWithTrend":      s_macd,
 "RSIDirectionalWithTrend":     s_rsi_fast,
 "RSIDirectionalWithTrendSlow": s_rsi_slow,
 "EMAPriceCrossoverWithThreshold": s_ema800,
}

def run_pair(df, fn, fee, t0, t1):
    buy, sell, sl, trail = fn(df)
    o=df.open.values; h=df.high.values; l=df.low.values; ts=df.index
    b=buy.fillna(False).values; s=sell.fillna(False).values
    trades=[]; pos=False; ent=0.0; peak=0.0; enti=0
    for i in range(len(df)-1):
        if not pos:
            if b[i] and ts[i+1]>=t0 and ts[i+1]<=t1:
                pos=True; ent=o[i+1]; peak=ent; enti=i+1
            continue
        peak=max(peak,h[i])
        stop = (peak*(1-sl)) if trail else (ent*(1-sl))
        if l[i]<=stop:                       # стоп внутри свечи
            px=min(stop,o[i]); trades.append((ts[enti],ts[i],ent,px,"stop")); pos=False; continue
        if s[i]:
            px=o[i+1]; trades.append((ts[enti],ts[i+1],ent,px,"signal")); pos=False
    out=[]
    for a,bb,e,x,why in trades:
        r=(x*(1-fee))/(e*(1+fee))-1.0
        out.append((a,bb,e,x,r,why))
    return out

def report(name, fn, fee, t0, t1, label):
    allt=[]
    for p in PAIRS:
        fp=os.path.join(DATA,p+".csv")
        if not os.path.exists(fp) or os.path.getsize(fp)<1000: continue
        df=pd.read_csv(fp)
        df["ts"]=pd.to_datetime(df.ts,unit="ms"); df=df.set_index("ts")
        df=df[df.index<=t1]
        if len(df)<900: continue
        allt+=run_pair(df,fn,fee,t0,t1)
    if not allt:
        print("  %-32s %s: сделок 0"%(name,label)); return None
    r=np.array([t[4] for t in allt])
    wr=100.0*(r>0).mean()
    print("  %-32s %-9s сделок %4d · ср. %+6.2f%% · винрейт %5.1f%% · сумма %+8.1f%%"
          %(name,label,len(r),100*r.mean(),wr,100*r.sum()))
    return dict(n=len(r),avg=100*r.mean(),wr=wr,tot=100*r.sum())

CLAIM={"DoubleEMACrossoverWithTrend":(655,0.56),"MACDCrossoverWithTrend":(300,0.49),
       "RSIDirectionalWithTrend":(181,0.27),"RSIDirectionalWithTrendSlow":(108,0.91),
       "EMAPriceCrossoverWithThreshold":(272,1.31)}
if __name__=="__main__":
    fee=0.001
    t0=pd.Timestamp(IN_S); t1=pd.Timestamp(IN_E)
    t2=pd.Timestamp("2026-08-20")
    print("=== 1. ОКНО АВТОРА %s..%s, комиссия 0.1%% за сторону ==="%(IN_S,IN_E))
    ins={}
    for n,f in STRATS.items():
        r=report(n,f,fee,t0,t1,"in-sample"); ins[n]=r
        c=CLAIM[n]
        if r: print("      ЗАЯВЛЕНО: сделок %4d · ср. %+.2f%%   ⇒ расхождение по числу %+.0f%%, по средней %+.0f%%"
                    %(c[0],c[1],100*(r["n"]-c[0])/c[0],100*(r["avg"]-c[1])/abs(c[1])))
    print()
    print("=== 2. ВНЕ ВЫБОРКИ %s..%s (6.5 лет, которых автор не видел) ==="%(IN_E,"2026-08-20"))
    for n,f in STRATS.items(): report(n,f,fee,t1,t2,"out-of-sample")
    print()
    print("=== 3. ЧУВСТВИТЕЛЬНОСТЬ К ИЗДЕРЖКЕ (окно автора) ===")
    for fe in (0.0,0.001,0.002):
        print("  --- комиссия %.1f%% за сторону ---"%(fe*100))
        for n,f in STRATS.items(): report(n,f,fe,t0,t1,"")
