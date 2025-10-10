#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[5]:


state=Board(7,7)
state.board=[random.choice([0,1,2,3,4,5]) for _ in range(49)]
locations=Board(7,7)
locations.board=list(range(49))
locations


# In[6]:


state


# In[12]:


for diag,diag_locations in zip(state.diags(3),locations.diags(3)):
    if diag_locations[0]==30 or diag_locations[-1]==30:
        print(diag,"   ",diag_locations)


# In[15]:


player=1
ball=3
moves=[]
for length in [2,3,4,5,6,7]:
    for diag,diag_locations in zip(state.diags(length),locations.diags(length)):

        if diag[0]==player+ball and all([d==player for d in diag[1:]]):
            moves.append([diag_locations[0],diag_locations[-1]])

    for diag,diag_locations in zip(state.rows(length),locations.rows(length)):

        if diag[0]==player+ball and all([d==player for d in diag[1:]]):
            moves.append([diag_locations[0],diag_locations[-1]])

    for diag,diag_locations in zip(state.cols(length),locations.cols(length)):

        if diag[0]==player+ball and all([d==player for d in diag[1:]]):
            moves.append([diag_locations[0],diag_locations[-1]])


# In[16]:


moves


# In[ ]:




