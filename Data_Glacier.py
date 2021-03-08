#!/usr/bin/env python
# coding: utf-8

# #selam

# In[18]:


import pandas as pd
import seaborn as sbn
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[97]:


cab_data=pd.read_excel("Cab_Data.xlsx")


# In[99]:


cab_data


# In[113]:


city_cab=cab_data.groupby(["City","Company"])["PerKmProfit"].mean()


# In[114]:


city_cab


# In[62]:





# In[21]:


date=list(cab_data["Date of Travel"].astype(str).str.split("-"))


# In[22]:


date


# In[101]:


years=[]
for y in date:
    years.append(y[0])
cab_data["Year"]=years


# In[102]:


cab_data


# In[104]:


PerKmProfit=(cab_data["Price Charged"] - cab_data["Cost of Trip"]) / cab_data["KM Travelled"] 


# In[105]:


cab_data["PerKmProfit"]=PerKmProfit


# In[106]:


cab_data


# In[ ]:





# In[28]:


xy=cab_data.groupby(["Year","Company"])["PerKmProfit"].mean()


# In[29]:


xy


# In[14]:


xy=pd.DataFrame(xy)


# In[15]:


xy


# In[38]:


PerKmProfit=pd.read_excel("PerKmProfit.xlsx")


# In[39]:


PerKmProfit


# In[53]:


sbn.barplot(x="Year",y="PerKmProfit",hue="Company",data=PerKmProfit)


# In[107]:


p2016=cab_data[(cab_data.Year == "2016") & (cab_data.Company == "Pink Cab")]


# In[108]:


p2016


# In[87]:


plt.figure(figsize=(25,10))
sbn.barplot(x="City",y="PerKmProfit",data=p2016)


# In[90]:


p2017=cab_data[(cab_data.Year == "2017") & (cab_data.Company == "Pink Cab")]
plt.figure(figsize=(25,10))
sbn.barplot(x="City",y="PerKmProfit",data=p2017)


# In[91]:


p2018=cab_data[(cab_data.Year == "2018") & (cab_data.Company == "Pink Cab")]
plt.figure(figsize=(25,10))
sbn.barplot(x="City",y="PerKmProfit",data=p2018)


# In[93]:


y2016=cab_data[(cab_data.Year == "2016") & (cab_data.Company == "Yellow Cab")]
plt.figure(figsize=(25,10))
sbn.barplot(x="City",y="PerKmProfit",data=y2016)


# In[94]:


y2017=cab_data[(cab_data.Year == "2017") & (cab_data.Company == "Yellow Cab")]
plt.figure(figsize=(25,10))
sbn.barplot(x="City",y="PerKmProfit",data=y2017)


# In[95]:


y2018=cab_data[(cab_data.Year == "2018") & (cab_data.Company == "Yellow Cab")]
plt.figure(figsize=(25,10))
sbn.barplot(x="City",y="PerKmProfit",data=y2018)


# In[119]:


city=pd.read_csv("City.csv")


# In[5]:


Customer_ID=pd.read_csv("Customer_ID.csv")


# In[6]:


Transaction_ID=pd.read_csv("Transaction_ID.csv")


# In[109]:


cab_data


# In[9]:


Customer_ID


# In[121]:


city


# In[126]:


cab_data_city=pd.merge(city,cab_data,on=["City"])


# In[127]:


cab_data_city


# In[130]:


pink_cab_users=cab_data_city[cab_data_city.Company=="Pink Cab"]


# In[142]:


plt.figure(figsize=(25,15))
sbn.scatterplot(x="City",y="Users",data=pink_cab_users)


# In[143]:


yellow_cab_users=cab_data_city[cab_data_city.Company=="Yellow Cab"]


# In[144]:


plt.figure(figsize=(25,15))
sbn.scatterplot(x="City",y="Users",data=yellow_cab_users)


# In[ ]:




