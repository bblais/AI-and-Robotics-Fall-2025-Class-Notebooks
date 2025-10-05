#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


T=Table()

state=6
T[state]=Table()
T[state][3]=3
T[state][2]=3
T[state][1]=3

state=5
T[state]=Table()
T[state][3]=3
T[state][2]=3
T[state][1]=3

T


# In[3]:


state=Board(3,3)
state


# In[21]:


T=Table()

T[state]=Table()
T[state][3]=3
T[state][2]=3
T[state][1]=3

state[2]=1

T[state]=Table()
T[state][3]=3
T[state][2]=30
T[state][1]=3


# In[22]:


T


# In[23]:


print([weighted_choice(T[state]) for _ in range(60)])


# In[ ]:




