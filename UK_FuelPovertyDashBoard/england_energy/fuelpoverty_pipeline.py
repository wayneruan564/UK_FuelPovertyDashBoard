#!/usr/bin/env python
# coding: utf-8

# In[117]:


import pandas as pd
import geopandas as gpd

import plotly.express as px

from plotly import graph_objects as go

import pyproj


# In[118]:


df = pd.read_csv('england_energy/region.csv', encoding='utf-8')

fp = "topo_eer.json"
map_df = gpd.read_file(fp)


# In[119]:


latest = df.loc[df['Year'] == 2020]
latest


# In[89]:


#average_gap
x = pd.Series(latest[latest.columns[0]])
y = pd.Series(latest[latest.columns[-1]])

df_combine = pd.DataFrame({"Average Fuel Poverty Gap":y,
                          'EER13NM':x}).iloc[:-1 , :]

df_combine.head()


# In[90]:


energy


# In[97]:


energy = pd.read_csv('energyprice.csv')
#selecting gas price in winter only
winter = energy.iloc[:, [0,1,10,11]][energy['Quarter'] == 'Jan to Mar'].rename(columns={"Year and dataset code row": "Year"})
winter


# In[ ]:





# In[122]:


ne = df.iloc[:, [0,1,-1]][df['Region'] == 'All households']

# ne['percent_change'] = ne.iloc[:,2].pct_change()
ne


# In[ ]:





# In[123]:


merge = ne.merge(winter, on=["Year"])
merge


# In[ ]:





# In[124]:


# fig = px.line(merge, x="Year", y=merge.iloc[:,2].pct_change(), title='Change in average fuel poverty gap Real Terms')

# fig.add_trace(go.Scatter(x=merge["Year"], y=merge.iloc[:, -1].pct_change(),
#                     mode='lines',
#                     name='Real Term Electricity Price'))

# fig.add_trace(go.Scatter(x=merge["Year"], y=merge.iloc[:, -2].pct_change(),
#                     mode='lines',
#                     name='Real Term Gas Price'))

# fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




