# from numpy import array,dot
# from sklearn.linear_model import LinearRegression
from time import time
from redistimeseries.client import Client
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from fbprophet import Prophet
MSEC = 1
SEC = 1000 * MSEC
MINUTE = 60 * SEC
rts = Client(host='localhost',port=6379)
# Grab the time series
data=rts.range("Temperature",
                from_time=0,
                to_time=-1,
                bucket_size_msec=60*5, # In Seconds NOT milliseconds
                aggregation_type='avg'
)
time,value=res =zip(*data)
time=[datetime.fromtimestamp(x) for x in time]
df=pd.DataFrame(dict(ds=time,y=value))
m = Prophet(changepoint_prior_scale=0.02,interval_width=.95).fit(df)
future = m.make_future_dataframe(periods=48, freq='H')
fcst = m.predict(future)
fcst=fcst.set_index('ds')
fcst.to_csv('forecast.csv')
ax=fcst[['yhat','yhat_upper','yhat_lower']]['2020-2-1':'2020-2-4'].plot()
df.set_index('ds')['2020-2-1':'2020-2-4'].plot(ax=ax)
plt.savefig('output.png',dpi=120)