import pickle


# In[2]:


import pandas as pd 
import datetime
import yfinance as yf
import numpy as np
#import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
#import matplotlib.pyplot as plt
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode


# In[3]:


filename = 'classifier_model.sav'
clf = pickle.load(open(filename, 'rb'))


# In[4]:




today = datetime.date.today()
lastfive = today - datetime.timedelta(days=23)

day = today.strftime ("%d/%m/%Y")
five = lastfive.strftime ("%d/%m/%Y")


# In[5]:


import investpy


# In[6]:


stock_df = investpy.get_stocks_overview(country="Bangladesh", 
                        as_json=False, 
                        n_results=1000)

data = investpy.get_stock_historical_data(stock='AAPL',
                                        country='United States',
                                        from_date='01/01/2010',
                                        to_date='01/01/2020')


st.write(data)
# In[7]:

#st = list[[]]

option = list(( stock_df["name"]).unique())

opt = st.multiselect(
     'Which companies would you like?',
     (option))

st.write('You selected:', opt)

for index, item in enumerate(opt):
    opt[index] = stock_df.loc[stock_df["name"]==item]["symbol"].values[0]

 
st.write(opt)



