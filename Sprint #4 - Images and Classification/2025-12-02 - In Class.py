#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pylab import *
from classy import *


# In[2]:


images=image.load_images('images/digits')


# In[3]:


images=image.load_images('digits.zip/digits')


# In[4]:


im=images.data[1500]
im.shape


# In[5]:


images=image.load_images('digits.zip/digits',resize=(4,4))


# In[6]:


im=images.data[1500]
im.shape


# In[ ]:




