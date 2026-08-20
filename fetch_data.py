import json,os,sys,time,urllib.request
OUT="./data"; os.makedirs(OUT,exist_ok=True)
PAIRS=["BTCUSDT","LTCUSDT","ETHUSDT","XRPUSDT","ADAUSDT","XLMUSDT","XMRUSDT","DASHUSDT"]
START=1519862400000   # 2018-03-01
def get(sym,start):
    u=("https://data-api.binance.vision/api/v3/klines?symbol=%s&interval=1h&startTime=%d&limit=1000"%(sym,start))
    for a in range(4):
        try: return json.load(urllib.request.urlopen(u,timeout=25))
        except Exception as e:
            time.sleep(2*(a+1))
    return []
for s in PAIRS:
    p=os.path.join(OUT,s+".csv")
    if os.path.exists(p) and os.path.getsize(p)>1000: print("уже есть",s); continue
    rows=[]; t=START
    while True:
        k=get(s,t)
        if not k: break
        rows+= [(int(x[0]),float(x[1]),float(x[2]),float(x[3]),float(x[4]),float(x[5])) for x in k]
        nt=int(k[-1][0])+3600000
        if nt<=t or len(k)<1000: break
        t=nt
        if len(rows)%20000<1000: print(" ",s,len(rows),flush=True)
    with open(p,"w") as f:
        f.write("ts,open,high,low,close,volume\n")
        for r in rows: f.write("%d,%.8f,%.8f,%.8f,%.8f,%.4f\n"%r)
    print("СКАЧАНО %-9s %6d свечей"%(s,len(rows)),flush=True)
