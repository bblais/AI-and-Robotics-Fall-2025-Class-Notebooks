#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# Four functions to do:
# 
# 1. `initial_state()`   return the state for the start of the game
# 2. `valid_moves(state,player)` return a list of valid moves
# 3. `update_state(state, player, move )` return the new state
# 4. `win_status(state,player)` returns one of `"win"`,`"lose"`,`"stalemate"` or `None`

# In[2]:


def initial_state():
    state=Board(3,3)
    state.pieces=[".","X","O"]
    return state


# In[3]:


def valid_moves(state,player):

    moves=[]

    for location in range(9): 
        if state[location]==0:
            moves.append(location)

    return moves



# In[4]:


def update_state(state,player,move):
    new_state=state
    new_state[move]=player

    return new_state


# In[5]:


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


# In[6]:


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


# In[7]:


def show_state(state,player):
    print(state)


# In[8]:


def random_move(state,player):
    return random.choice(valid_moves(state,player))
random_agent=Agent(random_move)


# In[9]:


from Game.minimax import *
def minimax_move(state,player):
    values,actions=minimax_values(state,player,display=False)
    return top_choice(actions,values)
minimax_agent=Agent(minimax_move)


# ![image.png](attachment:79374413-5431-4bd6-b94e-87abab72db5e.png)

# In[10]:


state=Board(3,3)
for loc in [0,7,8]:
    state[loc]=2
for loc in [2,3,6]:
    state[loc]=1
state


# In[11]:


minimax_values(state,player=1)


# In[12]:


g=Game()
g.run(minimax_agent,random_agent)


# ## Skittle Agent

# In[13]:


def skittles_move(state,player,info):
    T=info.T   # table for the skittles
    learning=info.learning
    last_state=info.last_state
    last_action=info.last_action


    # if we haven't seen this state before, initialize it
    if state not in T:
        actions=valid_moves(state,player)
        T[state]=Table()
        for action in actions:
            T[state][action]=2  # start with 1 skittle for each action

    move=weighted_choice(T[state])

    if move is None:
        move=random_move(state,player)

        if learning:
            if last_state:
                T[last_state][last_action]-=1  # punish last action == remove one skittle
                if T[last_state][last_action]<0:
                    T[last_state][last_action]=0  # don't go below zero

    return move


def skittles_after(status,player,info):
    T=info.T   # table for the skittles
    learning=info.learning
    last_state=info.last_state
    last_action=info.last_action

    if learning:
        if status=='lose':
            T[last_state][last_action]-=1  # punish last action == remove one skittle
            if T[last_state][last_action]<0:
                T[last_state][last_action]=0  # don't go below zero


# In[28]:


skittles_agent=Agent(skittles_move)
skittles_agent.T=LoadTable("TTT Skittles Agent2.json")  # starts off empty
skittles_agent.post=skittles_after
skittles_agent.learning=True


# ## Running the Game

# In[29]:


g=Game()
g.run(minimax_agent,skittles_agent)


# In[17]:


skittles_agent.T


# # Stages of training
# 
# - training stage == learning, changing # of skittles
# - testing stage == fixed # of skittles, see how well it does
# - epoch -- number of training games before testing
# 

# In[18]:


epoch_number=200  # play 200 games, learning, and then test
N_test=100  # play 100 games, fixed skittles, see how well it does
N_train=500  # play 500 epochs, learning, changing skittles

total_number_of_games=epoch_number*N_train
total_number_of_games


# In[19]:


iteration_count=0
percentage_won_player1=[]
percentage_won_player2=[]
percentage_stalemate=[]
number_of_iterations=[]


# In[20]:


agent1=Agent(skittles_move)
agent1.T=Table()  # starts off empty
agent1.post=skittles_after
agent1.learning=True

agent2=Agent(skittles_move)
agent2.T=Table()  # starts off empty
agent2.post=skittles_after
agent2.learning=True


# In[21]:


from tqdm import tqdm


# In[22]:


for i in tqdm(range(epoch_number)):
    # training step
    agent1.learning=True
    agent2.learning=True

    g=Game(number_of_games=N_train)
    g.display=False
    result=g.run(agent1,agent2)

    # testing step
    agent1.learning=False
    agent2.learning=False

    g=Game(number_of_games=N_test)
    g.display=False
    result=g.run(agent1,agent2)

    iteration_count+=N_train


    percentage_won_player1.append(result.count(1)/N_test*100)
    percentage_won_player2.append(result.count(2)/N_test*100)
    percentage_stalemate.append(result.count(0)/N_test*100)
    number_of_iterations.append(iteration_count)


# In[23]:


SaveTable(agent1.T,"TTT Skittles Agent1.json")
SaveTable(agent2.T,"TTT Skittles Agent2.json")


# In[24]:


from matplotlib import pyplot as plt


# In[25]:


plt.plot(number_of_iterations,percentage_won_player1,'-o',label="Player 1")
plt.plot(number_of_iterations,percentage_won_player2,'-x',label="Player 2")
plt.plot(number_of_iterations,percentage_stalemate,'-s',label="Stalemate")
plt.legend()


# In[26]:


g=Game(number_of_games=100)
g.display=False
result=g.run(minimax_agent,agent2)
print(result)


# In[27]:


g=Game(number_of_games=100)
g.display=False
result=g.run(agent1,minimax_agent)
print(result)


# This was an amazing game.  I was player 1 (X) and skittles as player 2(O):
# 
#     ====
#      .  .  . 
#      .  .  . 
#      .  .  . 
#     
#     Player 1 moves 4
#      .  .  . 
#      .  X  . 
#      .  .  . 
#     
#     Player 2 moves 6
#      .  .  . 
#      .  X  . 
#      O  .  . 
#     
#     Player 1 moves 0
#      X  .  . 
#      .  X  . 
#      O  .  . 
#     
#     Player 2 moves 8
#      X  .  . 
#      .  X  . 
#      O  .  O 
#     
#     Player 1 moves 3
#      X  .  . 
#      X  X  . 
#      O  .  O 
#     
#     Player 2 moves 5
#      X  .  . 
#      X  X  O 
#      O  .  O 
#     
#     Player 1 moves 2
#      X  .  X 
#      X  X  O 
#      O  .  O 
#     
#     Player 2 moves 1
#      X  O  X 
#      X  X  O 
#      O  .  O 
#     
#     Player 1 moves 7
#      X  O  X 
#      X  X  O 
#      O  X  O 
#     
#     Neither player won:  stalemate
# 
# 
# 

# In[ ]:




