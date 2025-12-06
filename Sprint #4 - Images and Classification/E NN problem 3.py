#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pylab import *
from classy import *


# In[2]:


images=image.load_images('images/hawkins_bitmaps subset/clean')


# In[3]:


data=image.images_to_vectors(images)


# In[4]:


data_train,data_test=split(data)


# In[5]:


C=BackProp([
    Input(shape=(1024,)),  # number of inputs
    Dense(features=15),  # hidden
    ReLU(),
    Dense(features=15),  # hidden
    ReLU(),
    Dense(features=7),  # output = number of categories
    ],learning_rate=0.001
)


# In[6]:


C.fit(data_train.vectors,data_train.targets,epochs=1000)
plot(C.training_accuracies,'.-',lw=1)

print("On train: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On test: ",C.percent_correct(data_test.vectors,data_test.targets))


# In[ ]:




