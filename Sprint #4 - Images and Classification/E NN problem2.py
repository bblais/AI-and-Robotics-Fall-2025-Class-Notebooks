#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pylab import *
from classy import *


# In[2]:


images=image.load_images('images/hawkins_bitmaps subset/clean')


# In[3]:


data=image.images_to_vectors(images)


# In[6]:


data_train,data_test=split(data,test_size=0.3)
#data_train,data_test=split(data)


# In[7]:


C=BackProp(
    [Input(shape=(1024,)), 
     Dense(features=15), 
     ReLU(), 
     Dense(features=15), 
     ReLU(), 
     Dense(features=7),], learning_rate=0.001)


# In[8]:


C.fit(data_train.vectors,data_train.targets,epochs=1000)
plot(C.training_accuracies,'.-',lw=1)
print('train: ', C.percent_correct(data_train.vectors,data_train.targets))
print('test: ', C.percent_correct(data_test.vectors,data_test.targets))


# In[ ]:




