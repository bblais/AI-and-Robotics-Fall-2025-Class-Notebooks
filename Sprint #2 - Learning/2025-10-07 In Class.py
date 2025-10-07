#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


b1=Board(3,3)
b1.board=list(range(9))
b2=Board(3,3)
b2.board=list(range(10,19))

b3=Board(3,3)
b3.board=list(range(20,29))


# In[3]:


str(b1)


# In[4]:


def combine_boards(b1,b2,b3):
    s1=str(b1)[:-1]
    s2=str(b2)[:-1]
    s3=str(b3)[:-1]

    S=''
    for l1,l2,l3 in zip(s1.split('\n'),s2.split('\n'),s3.split('\n')):
        S+=l1+"| "+l2+"| "+l3+"\n"

    return S




# In[5]:


print(combine_boards(b1,b2,b3))


# In[ ]:





# In[7]:


state[4]


# In[8]:


def show_state(state):

    S=""
    for r in range(3):
        S1=""
        for c in range(3):
            b=state[r,c]
            b_str=str(b)

    S=''
    for l1,l2 in zip(s1.split('\n'),s2.split('\n')):
        S+=l1+"| "+l2+"\n"

    return S



# In[28]:


def initial_state():
    board=Board(3,3)
    board[0]=1
    board[2]=11
    board[8]=2
    board[6]=22

    moves_list=[]
    return board,moves_list


# In[29]:


state=initial_state()
state


# In[12]:


def valid_moves(state,player):

    board,moves_list=state

    if len(moves_list)==3:
        return [  [-1,-1]  ]   # this is the end-turn move

    if player==1:
        if 11 in moves_list:  # only a player move
            moves=state.moves(1,"n","s","e","w")
        else:
            moves=state.moves(1,"n","s","e","w")+state.moves(11,"n","s","e","w")
    elif player==2:
        if 22 in moves_list:
            moves=state.moves(2,"n","s","e","w")
        else:
            moves=state.moves(2,"n","s","e","w")+state.moves(22,"n","s","e","w")
    else:
        raise ValueError("You can't get there from here")

    moves.append([-1,-1])
    return moves


# In[13]:


valid_moves(state,2)


# In[14]:


def win_status(state,player):
    other_player=3-player
    if not valid_moves(state,other_player):
        return "win"


# In[23]:


def update_state(state,player,move):
    board,moves_list=state
    start,end=move

    if end<=0:
        return board,[]


    board[end]=board[start]
    board[start]=0
    moves_list.append(board[end])

    return board,moves_list


# In[24]:


def show_state(state,player):
    print(state)


# In[25]:


def repeat_move(state,player,move):
    board,moves_list=state  
    start,end=move

    if end<=0:
        return False

    if len(moves_list)<3:
        return True
    else:
        return False


# In[26]:


def random_move(state,player):
    return random.choice(valid_moves(state,player))
random_agent=Agent(random_move)


# In[27]:


g=Game()
g.run(random_agent,random_agent)


# In[31]:


state=Board(4,5)
state[0]=state[6]=state[12]=1
board=Board(4,5)
board.board=list(range(20))

player=1
for a,b,c in board.diags(3):
    if state[a]==player and state[b]==player and state[c]==player:
        print("win")


# In[32]:


for a,b,c in state.diags(3):
    if a==player and b==player and c==player:
        print("win")


# In[33]:


state=Board(4,5)
state.show_locations()


# In[35]:


i=16
player=0
row,col=state.row(i),state.col(i)
row,col

state[row,col]



# In[36]:


def initial_state():
    state=Board(3,3)
    for i in [0,1,2]:
        state[i]=1
    for i in [6,7,8]:
        state[i]=2

    return state



# In[39]:


state=initial_state()
state


# In[41]:


def show_state(state,player):
    print(state)


# In[42]:


def update_state(state,player,move):
    start,end=move

    state[start]=0
    state[end]=player

    return state


# In[43]:


state=initial_state()
show_state(state,1)


# In[45]:


state=update_state(state,1, [1,4])
show_state(state,1)


# In[46]:


state.show_locations()


# In[ ]:


if state[start]==1 and state[start+5]==0:
    moves.append( [start,start+5]  )

