#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pylab import *


# In[2]:


from classy import *


# In[3]:


data = load_csv('data/wine.csv')


# In[4]:


data.vectors.shape


# In[5]:


data.target_names


# In[6]:


data.feature_names


# In[7]:


subset=extract_features(data,[0,1])
plot2D(subset)


# # Naive Bayes

# In[8]:


C=NaiveBayes()


# In[9]:


data_train,data_test=split(data,test_size=0.3)


# In[10]:


get_ipython().run_cell_magic('time', '', 'C.fit(data_train.vectors,data_train.targets)\n')


# In[11]:


print('train: ', C.percent_correct(data_train.vectors,data_train.targets))
print('test: ', C.percent_correct(data_test.vectors,data_test.targets))


# In[12]:


C.means


# # KNN

# In[13]:


C = kNearestNeighbor(k=3)


# In[14]:


get_ipython().run_cell_magic('time', '', 'C.fit(data_train.vectors,data_train.targets)\n')


# In[15]:


print('train: ', C.percent_correct(data_train.vectors,data_train.targets))
print('test: ', C.percent_correct(data_test.vectors,data_test.targets))


# # CSC

# In[16]:


C = CSC()


# In[17]:


get_ipython().run_cell_magic('time', '', 'C.fit(data_train.vectors,data_train.targets)\n')


# In[18]:


print('train: ', C.percent_correct(data_train.vectors,data_train.targets))
print('test: ', C.percent_correct(data_test.vectors,data_test.targets))


# In[19]:


C.centers


# In[20]:


C.radii


# In[21]:


C.targets


# In[ ]:





# KNN and CSC performed very poorly on the test data, and Naive Bayes was more consistent and got about 70% for both. CSC had 100% training accuracy and overfit the data.

# # neural networks

# In[22]:


C=BackProp([Input(shape=(13,)), Dense(features=3)], learning_rate=0.01)


# In[23]:


C.fit(data_train.vectors,data_train.targets,epochs=500)
plot(C.training_accuracies,'.-',lw=1)


# In[24]:


print('train: ', C.percent_correct(data_train.vectors,data_train.targets))
print('test: ', C.percent_correct(data_test.vectors,data_test.targets))


# In[25]:


C=BackProp([Input(shape=(13,)), Dense(features=5), ReLU(), Dense(features=3)], learning_rate=0.001)


# # digits

# In[26]:


images=image.load_images('images/digits')


# In[27]:


data=image.images_to_vectors(images)


# In[28]:


data_train,data_test=split(data,test_size=0.3)


# In[29]:


C=BackProp(
    [Input(shape=(64,)), 
     Dense(features=15), 
     ReLU(), 
     Dense(features=15), 
     ReLU(), 
     Dense(features=10)], learning_rate=0.001)


# In[30]:


C.fit(data_train.vectors,data_train.targets,epochs=500)
plot(C.training_accuracies,'.-',lw=1)
print('train: ', C.percent_correct(data_train.vectors,data_train.targets))
print('test: ', C.percent_correct(data_test.vectors,data_test.targets))


# # hawkins
# How big are the images?
# How big are the vectors?  Does this make sense given the size of the images?
# Use multiple classification algorithms to classify the two Hawkins subset image sets
# Which algorithms work the best?  The worst?
# Are there any other issues (e.g. memory, time, etc...) that you encounter in this problem?

# In[31]:


images=image.load_images('images/hawkins_bitmaps subset/clean')


# In[32]:


data=image.images_to_vectors(images)


# In[33]:


data.vectors.shape


# In[34]:


data.target_names


# In[35]:


print(data.feature_names)


# In[36]:


data_train,data_test=split(data,test_size=0.3)


# In[37]:


C=BackProp(
    [Input(shape=(1024,)), 
     Dense(features=15), 
     ReLU(), 
     Dense(features=15), 
     ReLU(), 
     Dense(features=7)], learning_rate=0.001)


# In[38]:


C.fit(data_train.vectors,data_train.targets,epochs=1000)
plot(C.training_accuracies,'.-',lw=1)
print('train: ', C.percent_correct(data_train.vectors,data_train.targets))
print('test: ', C.percent_correct(data_test.vectors,data_test.targets))


# In[ ]:


C=NaiveBayes()
data_train,data_test=split(data,test_size=0.3)

C.fit(data_train.vectors,data_train.targets)
print('train: ', C.percent_correct(data_train.vectors,data_train.targets))
print('test: ', C.percent_correct(data_test.vectors,data_test.targets))


# In[ ]:


C=CSC()
data_train,data_test=split(data,test_size=0.3)

C.fit(data_train.vectors,data_train.targets)
print('train: ', C.percent_correct(data_train.vectors,data_train.targets))
print('test: ', C.percent_correct(data_test.vectors,data_test.targets))


# In[ ]:


C=kNearestNeighbor(k=5)
data_train,data_test=split(data,test_size=0.3)

C.fit(data_train.vectors,data_train.targets)
print('train: ', C.percent_correct(data_train.vectors,data_train.targets))
print('test: ', C.percent_correct(data_test.vectors,data_test.targets))


# In[ ]:




