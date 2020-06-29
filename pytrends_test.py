# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:00:38 2020

@author: 

This is from the following website:
    https://pypi.org/project/pytrends/
    https://towardsdatascience.com/google-trends-api-for-python-a84bc25db88f
"""

#========================Initialization============================
import pytrends
import os
import pandas as pd                        
from pytrends.request import TrendReq
# import the method TrendReq from pytrends.request to connect to Google first
pytrend = TrendReq()
os.chdir(r"C:\Users\admin\Box\CODING\Github\Summer-Research-2020")


#========================Interest By Region========================
# Choose the term to be searched as "Chinese virus"
pytrend.build_payload(kw_list=['Chinese virus'])
df = pytrend.interest_by_region()
df.head(10)
df.reset_index().plot(x='geoName', y='Chinese virus', figsize=(120, 10), kind='bar')
# The table is very diaspora, we want to filter the data to contain only numbers above a treshold
df = df[(df['Chinese virus']>=20)]
df = df.sort_values(by=['Chinese virus'], ascending=False) # sort the data
df.reset_index().plot(x='geoName', y='Chinese virus', figsize=(30, 10), kind='bar')


#========================Daily Search Trends========================
# Get Google Hot Trends data
df = pytrend.trending_searches(pn='united_states')
df.head()
df = pytrend.today_searches(pn='US') # For today's searches


#===========================Related Queries==========================
# Let us see what are the related queries for the topic "Coronavirus"
# When you want to change the topic name just run the following code again with the new name as the parameter
pytrend.build_payload(kw_list=['Chinese virus'])

# Related Queries, returns a dictionary of dataframes
related_queries = pytrend.related_queries()
related_queries.values()

# Related Topics, returns a dictionary of dataframes
related_topic = pytrend.related_topics()
related_topic.values()




















