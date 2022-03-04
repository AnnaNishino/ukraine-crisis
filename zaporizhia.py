#!/usr/bin/env python
# coding: utf-8

# In[23]:


import requests as rq
from datetime import datetime, timedelta, timezone
import pandas as pd


# In[11]:


for _ in range(10):
    try:
        html = rq.get('https://www.npp.zp.ua/uk/safety/arms#', timeout=120)
    except:
        pass
    else:
        break
else:
    pass


# In[14]:


df = pd.read_html(html.text)[0]


# In[15]:


df


# In[31]:


df.to_csv('data/'+datetime.now(timezone(timedelta(hours=+2))).strftime('%Y-%m-%d_%H:%M:%S')+'.csv', encoding='utf_8_sig')


# In[ ]:




