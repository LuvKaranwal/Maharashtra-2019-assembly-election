#!/usr/bin/env python
# coding: utf-8

# ## Importing libraries 

# In[1]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# In[2]:


os.chdir("E:\Projects\Maharastra election poll visualization")
os.getcwd()


# In[3]:


#vs - vote share
vs = pd.read_csv("vote share.csv")
vs = vs.iloc[0:len(vs)-1,].sort_values(by=['%'],ascending = False)
vs


# ## 1. Hovering pie chart for vote share percentage in 8 major parties, NOTA and remaining all others.  

# In[4]:


# Creating dataset 
parties = []
for party in vs.iloc[0:9,0]:
    parties.append(party)

parties.append("All remaining")
    
vote_percentages = []
for vote in vs.iloc[0:9,2]:
    vote_percentages.append(vote)

remaining_sum = 0
for perc in vs.iloc[9:,2]:
    remaining_sum += perc

vote_percentages.append(remaining_sum)
  
fig = go.Figure(go.Pie(
    title="Maharashtra 2019 assembly election vote share",
    name="",
    values = vote_percentages,
    labels = parties,
    text = parties,
    hovertemplate = "%{label}: <br>Vote percentage: %{percent} </br>"
))

fig.show()


# ## 2.Bar graph for Total Seats won by parties

# In[5]:


import plotly.express as px


# fig = px.bar(vs, x="party name", y="seats", color="medal", title="Long-Form Input")
fig = px.bar(vs, x="party name", y="Seats", title="Total sets acquired by parties", text='Seats')
fig.update_traces(textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()


# In[6]:


# rwso - region wise seat occupancy
rwso = pd.read_csv("Region wise seat occupancy.csv")
rwso = rwso.iloc[0:6,]
rwso


# ## 3.Region wise distribution of seats

# In[7]:


import plotly.express as px


# fig = px.bar(vs, x="party name", y="seats", color="medal", title="Long-Form Input")
fig = px.bar(rwso, x="Region", y="Total seats", title="Total seats in different regions", text='Total seats')
fig.update_traces(textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()


# ## 4.Region wise occupancy of seats by different parties

# In[8]:


import plotly.express as px

parties=['Bharatiya Janata Party', 'Shiv Sena', 'Indian National Congress', 'Nationalist Congress Party', 'Others']
fig = px.bar(rwso, x="Region", y=parties, title="Seat occupancy by parties in different regions", barmode="group")

fig.show()

