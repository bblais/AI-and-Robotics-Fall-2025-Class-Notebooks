#!/usr/bin/env python
# coding: utf-8

# on the anaconda prompt do:
# 
# pip install "git+https://github.com/bblais/classy" --upgrade

# In[1]:


from pylab import *
from classy import *


# In[2]:


data=load_excel('data/iris.xls')


# ## Look at the data

# In[3]:


data.vectors.shape


# In[5]:


data.targets


# In[6]:


data.target_names


# In[7]:


data.feature_names


# In[11]:


subset=extract_features(data,[0,1])
plot2D(subset)


# ## Classification

# In[13]:


C=NaiveBayes()


# In[14]:


data_train,data_test=split(data,test_size=0.2)


# In[23]:


get_ipython().run_cell_magic('time', '', 'C.fit(data_train.vectors,data_train.targets)\n')


# In[25]:


print("On training set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On test set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[26]:


C.means


# In[38]:


C.predict(array([ [1,2.2,1.2,4.4] ,[.5,.5,4,3] ] ))


# In[ ]:





# In[39]:


C=kNearestNeighbor(k=3)


# In[40]:


get_ipython().run_cell_magic('time', '', 'C.fit(data_train.vectors,data_train.targets)\n')


# In[41]:


print("On training set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On test set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[42]:


C.predict(array([ [1,2.2,1.2,4.4] ,[.5,.5,4,3] ] ))


# In[ ]:





# In[43]:


C=CSC()


# In[44]:


get_ipython().run_cell_magic('time', '', 'C.fit(data_train.vectors,data_train.targets)\n')


# In[45]:


print("On training set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On test set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[46]:


C.predict(array([ [1,2.2,1.2,4.4] ,[.5,.5,4,3] ] ))


# In[47]:


C.centers


# In[48]:


C.radii


# In[49]:


C.targets


# In[ ]:




