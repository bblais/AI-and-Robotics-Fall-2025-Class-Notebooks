#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pylab import *


# In[3]:


im=imread('images/cats.jpg')


# In[4]:


imshow(im)


# In[5]:


im.shape


# In[6]:


arr=(rand(10)*100).round()
arr


# In[7]:


arr.shape


# In[8]:


arr[3]


# In[9]:


arr[3:7]


# In[10]:


arr[7:10]


# In[11]:


arr=(rand(4,10)*100).round()
arr


# In[14]:


arr[1,:]


# In[15]:


arr[1,3:]


# In[16]:


arr[0:2,3:]


# # go back to cats

# In[17]:


imshow(im)


# In[18]:


im.shape


# In[24]:


figure(figsize=(12,8))
subplot(1,3,1)
imshow(im[:,:,0],cmap=cm.gray)

subplot(1,3,2)
imshow(im[:,:,1],cmap=cm.gray)

subplot(1,3,3)
imshow(im[:,:,2],cmap=cm.gray)


# In[25]:


imshow(im)


# In[26]:


subimage=im[400:800,710:1100,:]
imshow(subimage)


# In[27]:


im=imread('images/cats.jpg')
im.shape


# In[28]:


im=imread('images/cat1.png')
im.shape


# In[33]:


labels=['red','green','blue','alpha']
for i in range(4):
    figure()
    imshow(im[:,:,i],cmap=cm.gray)
    title(labels[i])
    colorbar()


# In[ ]:




