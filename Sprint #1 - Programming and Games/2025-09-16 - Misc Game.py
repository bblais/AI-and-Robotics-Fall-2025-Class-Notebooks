#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


state=Board(3,3,3)
state


# In[3]:


state.show_locations()


# In[8]:


state[9]=1
state[10]=1
state[11]=1


# In[12]:


def three_in_a_row(state,a,b,c,player):
    if state[a]==player and state[b]==player and state[c]==player:
        return True
    else:
        return False


# In[13]:


three_in_a_row(state,0,1,2,player=1)


# In[14]:


three_in_a_row(state,9,10,11,player=1)


# In[15]:


def check_board(board,player):
    if three_in_a_row(state,0,1,2,player):
        return True
    if three_in_a_row(state,3,4,5,player):
        return True
    if three_in_a_row(state,6,7,8,player):
        return True
    if three_in_a_row(state,0,3,6,player):
        return True
    if three_in_a_row(state,1,4,7,player):
        return True
    if three_in_a_row(state,2,5,8,player):
        return True
    if three_in_a_row(state,0,4,8,player):
        return True
    if three_in_a_row(state,2,4,6,player):
        return True

    else:
        return False


# In[16]:


check_board(state,player=1)


# In[17]:


state


# In[ ]:


def win_status(state,player):

    locations=[9,10,11,12,13,14,15,16,17]
    small_board=Board(3,3)
    for i in range(9):
        small_board[i]=state[locations[i]]

    if check_board(small_board,player):
        return True
    else:
        return False







