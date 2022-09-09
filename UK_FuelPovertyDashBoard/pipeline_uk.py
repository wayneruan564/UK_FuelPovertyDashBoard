#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import geopandas as gpd

import pyproj


# In[3]:


#geo map
fp = "topo_eer.json"
map_df = gpd.read_file(fp)

#average fuel poverty gap data by region, all household
gap = pd.read_csv('england_energy/region.csv', encoding='utf-8')

#price of gas and electricity in the winter ('January to March')
energy = pd.read_csv('energyprice.csv')
# energy

payment = pd.read_csv('england_energy/data/electricityPayment.csv', encoding='utf-8')

#unemployment info
u_df = pd.read_csv('england_energy/unemployment.csv')

#efficiency of houses overall
efficiency_df = pd.read_csv('england_energy/data/energyefficiency.csv')

#costs of energy bill by houses
housetype_en = pd.read_csv('england_energy/data/england_housetype.csv').head(6)

#electricity bill of houses
housetype_region = pd.read_csv('england_energy/energycost_housetype.csv')


# In[ ]:





# In[4]:


df = gap.drop(columns= ['Proportion of not fuel poor households within group (%)', 
                       'Number of households (thousands) - Not fuel poor', 
                       'Total number of households (thousands)'])


# In[5]:


#selecting gas price in winter only
winter = energy.iloc[:, [0,1,10,11]][energy['Quarter'] == 'Oct to Dec'].rename(columns={"Year and dataset code row": "Year"})


# In[6]:


#combining average fuel poverty gap data with winter gas price. 
merge = pd.merge(df, winter, how="inner", on=['Year']).drop(columns= ['Quarter'])


# In[7]:


df_pay = payment.drop(columns= ['Proportion of not fuel poor households within group (%)', 
                       'Number of households (thousands) - Not fuel poor', 
                       'Total number of households (thousands)'])


# In[8]:


debit = df_pay.loc[df_pay['Method of electricity payment'] == 'Direct debit']
credit = df_pay.loc[df_pay['Method of electricity payment'] == 'Standard credit']
prepay = df_pay.loc[df_pay['Method of electricity payment'] == 'Prepayment']
all_household = df_pay.loc[df_pay['Method of electricity payment'] == 'All households']


# In[9]:


n = -1

o = pd.Series(['Direct Debit', 'Standard Credit', 'PrePayment'])
p = pd.Series([debit[debit.columns[n]].pct_change().iloc[-1,], credit[credit.columns[n]].pct_change().iloc[-1,], prepay[prepay.columns[n]].pct_change().iloc[-1,]])

q = pd.DataFrame({"Percent change in Fuel Poverty Gap":p,
                          'Method':o})


# In[10]:


#line graph showing trend between energy price and fuel poverty gap.

query = 'All households'
year = 2020


# In[11]:


#data description
fp_ranking = df.iloc[:,[0,2]][df['Year'] == year].head(9).sort_values(by=['Proportion of fuel poor households within group (%)'], ascending = False).reset_index(drop=True)
fp_ranking


# In[12]:


#data description
gap_ranking = df.iloc[:,[0,-1]][df['Year'] == year].head(9).sort_values(by=['Average fuel poverty gap Real Terms'], ascending = False).reset_index(drop=True)
gap_ranking


# In[13]:


household_count = gap[gap['Year'] == year].iloc[:,[0,-4]]


# In[14]:


#ranking region by  household count population 
household_rank = household_count.head(9).sort_values(by=['Total number of households (thousands)'], ascending = False).reset_index(drop=True)


# In[ ]:





# In[15]:


unemploymentRate = u_df.iloc[:, [0,-1]].sort_values(by=['Jun-22'], ascending = False).reset_index(drop=True)

delete_row = unemploymentRate.loc[unemploymentRate['Region'] == 'All households'].index


# In[ ]:





# In[16]:


house_cost = housetype_region.loc[housetype_region['Country or region name'] == query].T.reset_index().tail(5).rename(columns={0: "Cost", 'index':"House Type"})
house_cost


# In[ ]:





# In[17]:


#statistic to show up on dashboard. hinging on query
fuelpoverty_pcg = gap.loc[gap['Region'] == query][gap.columns[3]].iloc[-1]
fuelpoverty_gp = gap.loc[gap['Region'] == query][gap.columns[-1]].iloc[-1]
unemployment_r = unemploymentRate.loc[unemploymentRate['Region'] == query][unemploymentRate.columns[-1]].iloc[-1]


# In[ ]:





# In[18]:


#data used for line chart fig 1.

fuelgap_column = merge.iloc[:,-3]
electricity_column = merge.iloc[:, -2]
gas_column = merge.iloc[:, -1]


# In[ ]:





# In[19]:


year_column = merge.iloc[:,1].unique()
year_column


# In[ ]:





# In[ ]:




