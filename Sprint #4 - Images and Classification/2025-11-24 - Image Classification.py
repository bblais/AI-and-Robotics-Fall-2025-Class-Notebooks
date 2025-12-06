#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pylab import *
from classy import *


# ## Loading the data, converting to vectors

# In[2]:


images=image.load_images('images/digits')


# In[4]:


images=image.load_images('digits.zip/digits')


# In[8]:


images.keys()


# In[9]:


len(images.data)


# In[5]:


im=images.data[1500]
im.shape


# In[16]:


images.targets[1500]


# In[18]:


images.target_names[8]


# In[19]:


imshow(im,cmap=cm.gray)


# In[20]:


data=image.images_to_vectors(images)


# In[21]:


data.targets


# In[22]:


data.target_names


# In[23]:


data_train,data_test=split(data)


# ## Classify the vectors

# In[27]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)
print("On train: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On test: ",C.percent_correct(data_test.vectors,data_test.targets))



# In[29]:


C.means.shape


# ### Visualize the internals of the classifier

# In[31]:


which_category=0
prototype=C.means[which_category,:]
category_name=data.target_names[which_category]
prototype.shape


# In[32]:


prototype=prototype.reshape(8,8)
imshow(prototype,cmap=cm.gray)
title(category_name)


# In[33]:


which_category=4
prototype=C.means[which_category,:]
category_name=data.target_names[which_category]
prototype.shape


# In[34]:


prototype=prototype.reshape(8,8)
imshow(prototype,cmap=cm.gray)
title(category_name)


# In[ ]:





# In[35]:


C=kNearestNeighbor(k=5)
C.fit(data_train.vectors,data_train.targets)
print("On train: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On test: ",C.percent_correct(data_test.vectors,data_test.targets))



# In[40]:


C=CSC()
C.fit(data_train.vectors,data_train.targets)
print("On train: ",C.percent_correct(data_train.vectors,data_train.targets))
print("On test: ",C.percent_correct(data_test.vectors,data_test.targets))



# ### Visualize the internals of the classifier

# In[41]:


C.centers


# In[42]:


C.centers.shape


# In[43]:


C.targets


# In[44]:


which_center=4
prototype=C.centers[which_center,:]
category_name=data.target_names[C.targets[which_center]]
prototype.shape


# In[85]:


prototype=prototype.reshape(8,8)
imshow(prototype,cmap=cm.gray)
title(category_name)
colorbar()


# ## make a prediction

# In[86]:


new_image=imread('images/digits/six/1734.png')
imshow(new_image,cmap=cm.gray)
colorbar()


# In[87]:


new_image=imread('images/digits/six/1734.png')
new_image=new_image*255
imshow(new_image,cmap=cm.gray)
colorbar()


# In[88]:


new_image.shape


# In[89]:


new_vector=new_image.reshape(1,64)
new_vector.shape


# In[90]:


C.predict(new_vector)[0]


# In[91]:


data.target_names[C.predict(new_vector)[0]]


# In[ ]:




