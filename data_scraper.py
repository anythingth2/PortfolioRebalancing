#%%
import ccxt
import pandas as pd
import datetime
import tqdm
#%%
symbol = 'ETH/USDT'
timeframe = '1m'

exchange = ccxt.ftx()
dfs = []
for dt in tqdm.tqdm(pd.date_range('2021-09-04 16:00:00', datetime.datetime.now())):
    timestamp = int(dt.to_pydatetime().timestamp() * 1000)

    data = exchange.fetch_ohlcv(symbol, timeframe, since=timestamp, limit=None)

    df = pd.DataFrame(data, columns=['unix', 'open', 'high', 'low', 'close', 'volumn'])
    df['date'] = pd.to_datetime(df['unix'], unit='ms')
    df = df[['unix', 'date', 'open', 'high', 'low', 'close', 'volumn']]
    dfs.append(df)
#%%
ohlcv_df = pd.concat(dfs)
ohlcv_df.to_csv('dataset/raw_ohlcv.csv', index=False)


# %%
