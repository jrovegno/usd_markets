
# coding: utf-8

# In[1]:

import pandas as pd
import Quandl
import pandas_datareader.data as web


# In[2]:

start = pd.Timestamp("2002-01-02")
end = pd.Timestamp("2015-12-30")
online = False


# In[3]:

if online:
    ipsa = web.DataReader("^IPSA", 'yahoo', start, end)
    usdclp = Quandl.get("CURRFX/USDCLP")
    ipsa.to_csv('ipsa_clp.csv')
    usdclp.to_csv('usdclp.csv')
else:
    ipsa = pd.read_csv('ipsa_clp.csv', index_col='Date', parse_dates=True)
    usdclp = pd.read_csv('usdclp.csv', index_col='Date', parse_dates=True)


# In[4]:

df = pd.DataFrame()
df['ipsa_clp'] = ipsa[u'Adj Close']
df['usdclp'] = usdclp.Rate
df['ipsa_usd'] = df.ipsa_clp / df.usdclp


# In[5]:

ax = df.plot(subplots=True, figsize=(10, 10), sharex=True)
fig = ax[0].get_figure()
fig.savefig('ipsa_usd_clp.png')
