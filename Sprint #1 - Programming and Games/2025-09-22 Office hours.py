#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


state=Board(4,4)
state[1]=1
state[2]=2
state[3]=1
state[4]=1
state[5]=2
state


# In[5]:


# count all the player 0 pieces
count=0
for location in range(16):
    if state[location]==0:
        count=count+1

print(count)


# In[ ]:




