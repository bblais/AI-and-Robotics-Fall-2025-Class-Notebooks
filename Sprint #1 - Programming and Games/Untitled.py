#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


def initial_state():

    board=Board(5,5)
    capture_count=0

    return board,capture_count


# In[ ]:


def valid_moves(state,player):
    board,capture_count=state




# In[3]:


def update_state(state,player,move):
    board,capture_count=state

    capture_count+=1

    new_state=board,capture_count

    return new_state


# In[5]:


state=Board(6,7)
state.show_locations()
state


# In[ ]:


player=1
for start in [0,1,2,3,...20]:  # 4 down
    if state[start]==player and state[start+7]==player and state[start+14]==player and state[start+21]==player:
        return "win"


# In[ ]:





# In[ ]:


move_input=input("Enter your move as a location or start,end: ")
parts=move_input.split(",")
if len(parts)==1:
    move=int(parts[0])
else:
    move=(int(parts[0]),int(parts[1]))


# In[7]:


state=Board(4,5)
state.show_locations()
state


# In[11]:


state=Board(4,5)
move=2
player=1
new_state=state

if state[move+15]==0:
    new_state[move+15]=player
elif state[move+10]==0:
    new_state[move+10]=player
elif state[move+5]==0:
    new_state[move+5]=player
elif state[move]==0:
    new_state[move]=player
else:
    raise ValueError("You can't get there from here")

new_state


# In[ ]:




