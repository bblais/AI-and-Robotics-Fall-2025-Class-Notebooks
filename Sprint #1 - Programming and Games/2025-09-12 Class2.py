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


# In[7]:


def Kdiag(start):

    return [start-6,start-4,start+4,start+6]


# In[8]:


def valid_moves(state,player):
    moves=[]

    for start in range(25):
        if state[start]==player:
            end_locations=Kdiag(start)

            for end in end_locations:
                if state[end]==0:
                    moves.append((start,end))

    return moves


# In[ ]:




