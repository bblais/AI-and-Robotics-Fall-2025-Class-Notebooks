#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Game import *


# Four functions to do:
# 
# 1. `initial_state()`   return the state for the start of the game
# 2. `valid_moves(state,player)` return a list of valid moves
# 3. `update_state(state, player, move )` return the new state
# 4. `win_status(state,player)` returns one of `"win"`,`"lose"`,`"stalemate"` or `None`

# In[3]:


def initial_state():
    state=Board(3,3)
    state.pieces=[".","X","O"]
    return state


# In[4]:


def valid_moves(state,player):

    moves=[]

    for location in range(9): 
        if state[location]==0:
            moves.append(location)

    return moves



# In[5]:


def update_state(state,player,move):
    new_state=state
    new_state[move]=player

    return new_state


# In[6]:


def win_status(state,player):
    # 0  1  2 
    # 3  4  5 
    # 6  7  8 

    if player==1:
        other_player=2
    else:
        other_player=1

    if state[0]==state[1]==state[2]==player:
        return "win"
    if state[3]==state[4]==state[5]==player:
        return "win"
    if state[6]==state[7]==state[8]==player:
        return "win"
    if state[0]==state[3]==state[6]==player:
        return "win"
    if state[1]==state[4]==state[7]==player:
        return "win"
    if state[2]==state[5]==state[8]==player:
        return "win"
    if state[0]==state[4]==state[8]==player:
        return "win"
    if state[6]==state[4]==state[2]==player:
        return "win"

    if not valid_moves(state,other_player):
        return "stalemate"

    return None


# In[7]:


def human_move(state,player):
    print("Locations:")
    state.show_locations()
    print("Valid Moves:")
    print(valid_moves(state,player))

    while True:
        move=eval(input("Enter your move"))

        if move not in valid_moves(state,player):
            print("That is not a valid move")
        else:
            break

    return move

human_agent=Agent(human_move)


# In[8]:


def show_state(state,player):
    print(state)


# In[9]:


def random_move(state,player):
    return random.choice(valid_moves(state,player))
random_agent=Agent(random_move)


# In[10]:


from Game.minimax import *
def minimax_move(state,player):
    values,actions=minimax_values(state,player,display=False)
    return top_choice(actions,values)
minimax_agent=Agent(minimax_move)


# In[11]:


def table_move(state,player,info):
    T=info.T   # table for the skittles

    # if we haven't seen this state before, do random
    if state not in T:
        move=random_move(state,player)
        return move

    move=weighted_choice(T[state])

    if move is None:
        move=random_move(state,player)

    return move



# In[12]:


table_agent1=Agent(table_move)
table_agent1.T=LoadTable("TTT Skittles Agent1") 

table_agent2=Agent(table_move)
table_agent2.T=LoadTable("TTT Skittles Agent2") 


# In[14]:


g=Game()
g.run(table_agent1,minimax_agent)


# In[ ]:




