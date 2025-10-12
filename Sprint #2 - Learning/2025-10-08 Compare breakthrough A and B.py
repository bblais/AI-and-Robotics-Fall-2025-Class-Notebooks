#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


import breakthrough as B
import breakthrough_A as A


# In[7]:


states=[_.initial_state() for _ in [A,B]]
states[0].board,states[1].board


# In[9]:


states[0]==states[1]


# In[13]:


moves_A=A.valid_moves(states[0],1)
moves_A


# In[14]:


moves_B=B.valid_moves(states[0],1)
moves_B


# In[15]:


states[0].show_locations()


# In[ ]:




