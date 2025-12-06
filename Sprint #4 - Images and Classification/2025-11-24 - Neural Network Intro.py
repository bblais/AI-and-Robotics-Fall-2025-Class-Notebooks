#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pylab import *
from classy import *


# In[2]:


data=load_excel('data/iris.xls')


# In[3]:


data_train,data_test=split(data)


# # Perceptron
# 
# - single layer
# - linear units

# In[5]:


C=BackProp([
    Input(shape=(4,)),
    Dense(features=3),  # output = number of categories
    ],learning_rate=0.01
)


# In[6]:


C.output([6.9, 3.1, 5.4, 2.1])


# In[8]:


C.fit(data_train.vectors,data_train.targets,epochs=1000)
plot(C.training_accuracies,'.-',lw=1)


# In[10]:


print("On train: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On test: ",C.percent_correct(data_test.vectors,data_test.targets))


# In[11]:


C.output([6.9, 3.1, 5.4, 2.1])


# In[12]:


C=BackProp([
    Input(shape=(4,)),
    Dense(features=15),  # hidden
    ReLU(),
    Dense(features=3),  # output = number of categories
    ],learning_rate=0.001
)


# In[14]:


C.fit(data_train.vectors,data_train.targets,epochs=1000)
plot(C.training_accuracies,'.-',lw=1)

print("On train: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On test: ",C.percent_correct(data_test.vectors,data_test.targets))


# In[15]:


C.output([6.9, 3.1, 5.4, 2.1])


# In[16]:


C=BackProp([
    Input(shape=(4,)),
    Dense(features=15),  # hidden
    ReLU(),
    Dense(features=15),  # hidden
    ReLU(),
    Dense(features=3),  # output = number of categories
    ],learning_rate=0.001
)


# In[17]:


C.fit(data_train.vectors,data_train.targets,epochs=1000)
plot(C.training_accuracies,'.-',lw=1)

print("On train: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On test: ",C.percent_correct(data_test.vectors,data_test.targets))


# # Images

# In[18]:


images=image.load_images('images/digits')


# In[19]:


data=image.images_to_vectors(images)


# In[20]:


data_train,data_test=split(data)


# In[23]:


C=BackProp([
    Input(shape=(64,)),  # number of inputs
    Dense(features=15),  # hidden
    ReLU(),
    Dense(features=15),  # hidden
    ReLU(),
    Dense(features=10),  # output = number of categories
    ],learning_rate=0.001
)


# In[24]:


C.fit(data_train.vectors,data_train.targets,epochs=1000)
plot(C.training_accuracies,'.-',lw=1)

print("On train: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On test: ",C.percent_correct(data_test.vectors,data_test.targets))


# In[ ]:




