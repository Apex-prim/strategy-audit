# -*- coding: utf-8 -*-
"""Готовит рабочую папку freqtrade и переводит скачанные свечи в его формат.

Данные берутся с публичного зеркала Binance (data-api.binance.vision), потому
что основной API закрыт по геолокации, а собственный `download-data` freqtrade
ходит именно туда. Поэтому конвертируем, а не качаем повторно.
"""
import json
import sys as _sys
_sys.path.insert(0, "C:/tmp/audit")
import runlock as _rl
if not _rl.acquire("fetch"):      # общая папка свечей — один писатель
    raise SystemExit(2)
import atexit as _at
_at.register(lambda: _rl.release("fetch"))

import os
import sys

import pandas as pd

SRC = "C:/c/tmp/audit/data"
UD = "C:/tmp/audit/user_data"
PAIRS = {"BTCUSDT": "BTC_USDT", "LTCUSDT": "LTC_USDT", "ETHUSDT": "ETH_USDT",
         "XRPUSDT": "XRP_USDT", "ADAUSDT": "ADA_USDT", "XLMUSDT": "XLM_USDT",
         "XMRUSDT": "XMR_USDT", "DASHUSDT": "DASH_USDT"}

for d in ("data/binance", "strategies", "backtest_results"):
    os.makedirs(os.path.join(UD, d), exist_ok=True)

n = 0
for src_name, ft_name in PAIRS.items():
    p = os.path.join(SRC, src_name + ".csv")
    if not os.path.exists(p) or os.path.getsize(p) < 1000:
        print("  пропуск (нет данных):", src_name)
        continue
    df = pd.read_csv(p)
    df = df.rename(columns={"ts": "date"})
    df = df[["date", "open", "high", "low", "close", "volume"]]
    out = os.path.join(UD, "data", "binance", ft_name + "-1h.feather")
    df.reset_index(drop=True).to_feather(out)
    n += 1
    print("  %-10s -> %s  (%d свечей)" % (src_name, os.path.basename(out), len(df)))

cfg = {
    "max_open_trades": 8,
    "stake_currency": "USDT",
    "stake_amount": "unlimited",
    "tradable_balance_ratio": 0.99,
    "dry_run": True,
    "dry_run_wallet": 1000,
    "timeframe": "1h",
    "trading_mode": "spot",
    "margin_mode": "",
    "unfilledtimeout": {"entry": 10, "exit": 10, "unit": "minutes"},
    "entry_pricing": {"price_side": "same", "use_order_book": False,
                      "order_book_top": 1,
                      "price_last_balance": 0.0, "check_depth_of_market":
                      {"enabled": False, "bids_to_ask_delta": 1}},
    "exit_pricing": {"price_side": "same", "use_order_book": False,
                     "order_book_top": 1},
    "exchange": {
        "name": "binance", "key": "", "secret": "",
        "ccxt_config": {}, "ccxt_async_config": {},
        "pair_whitelist": [v.replace("_", "/") for v in PAIRS.values()],
        "pair_blacklist": [],
    },
    "pairlists": [{"method": "StaticPairList"}],
    "dataformat_ohlcv": "feather",
    "user_data_dir": UD,
    "datadir": os.path.join(UD, "data", "binance"),
    "strategy_path": os.path.join(UD, "strategies"),
    "internals": {"process_throttle_secs": 5},
}
with open(os.path.join(UD, "config.json"), "w") as f:
    json.dump(cfg, f, indent=2)

print("\nпар переведено: %d" % n)
print("конфиг: %s" % os.path.join(UD, "config.json"))
print("⚠ ключи биржи ПУСТЫЕ — бэктест их не требует и не должен")
