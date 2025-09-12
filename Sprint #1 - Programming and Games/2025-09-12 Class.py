#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


def initial_state():
    state=Board(4,5)
    return state


# In[3]:


state=initial_state()
state


# In[4]:


s='●'


# In[8]:


ord(s[0])


# In[9]:


chr(9679)


# In[10]:


ord('○')


# In[2]:


state=Board(5,5)
state


# In[3]:


state.show_locations()


# In[ ]:




