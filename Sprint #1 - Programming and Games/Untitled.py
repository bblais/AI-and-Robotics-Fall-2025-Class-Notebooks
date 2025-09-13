#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[3]:


state=Board(5,5)
state


# In[4]:


state.show_locations()


# In[5]:


def valid_moves(state,player):
    moves=[]


    if player==1:
        for location in [0,1,2,3,4,5,6,7,8,9,
                         10,11,12,13,14,15,16,17,18,19]:
            if state[location]==1 and state[location+5]==0:
                moves.append((location,location+5))


    return moves


# In[6]:


state=Board(5,5)
for i in range(5):
    state[i]=1

valid_moves(state,1)


# In[ ]:




