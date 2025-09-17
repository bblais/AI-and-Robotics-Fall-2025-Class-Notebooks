#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mplturtle import *


# In[8]:


reset()
for i in range(4):
    forward(100)
    right(90)

py.xlim([-50,110])
py.ylim([-120,20])


# In[10]:


from Game import *


# In[11]:


state=Board(4,5)
state.show_locations()


# In[ ]:


player=1
if state[0]==player and state[1]==player and state[2]==player:
    return 'win'




# In[15]:


state=Board(4,5)
state[0]=1
state[3]=1
state[6]=1


# In[16]:


player=1
for a,b,c in [[0,1,2],[3,4,5],[6,7,8],  # first 2 rows
              [0,3,6],[1,4,7],[2,5,8],
              [0,4,8],[2,4,6]  
             ]:
    if state[a]==player and state[b]==player and state[c]==player:
        print('win')


# In[ ]:


def valid_moves(state,player):

    for location in range(16):

        pieces=state[location]




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


def update_state(state,player,move):

    piece,location=move

    new_state=state




    return new_state


# In[1]:


for start,end in [[4,5],[6,7]]:
    print(start,"end",end)


# In[ ]:


state=initial_state()
player=2
move=["S",2]
update_state(state,player,move)


# In[ ]:


if state[0]==1 and state[4]==2 and state[8]==1:
    return "win"

if not valid_moves(state,player):
    return "stalemate"


# In[ ]:





# In[ ]:


if player==1:
    other_player=2
else:
    other_player=1

for a,b,c in [[0,1,2],[3,4,5],[6,7,8],  # first 2 rows
              [0,3,6],[1,4,7],[2,5,8],
              [0,4,8],[2,4,6]  
             ]:
    if state[a]==0 and state[b]==other_player and state[c]==player:
        moves.append([c,a])
    if state[c]==0 and state[b]==other_player and state[a]==player:
        moves.append([a,c])




# In[3]:


from Game import *


# In[5]:


state=Board(3,3)
state.pieces=[".","S","O"]

state


# In[6]:


state[2]=1


# In[7]:


state


# In[ ]:




