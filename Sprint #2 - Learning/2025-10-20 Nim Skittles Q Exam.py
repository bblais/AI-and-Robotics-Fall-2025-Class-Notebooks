#!/usr/bin/env python
# coding: utf-8

# # Nim (21 Sticks Variant)
# 
# ## Setup
# - Start with **21 sticks** (or counters, stones, matches, etc.).  
# - Two players take turns.  
# 
# ---
# 
# ## Rules
# 1. On your turn, you must take **1, 2, or 3 sticks** from the pile.  
# 2. Players alternate turns.  
# 3. **The player forced to take the last stick loses.**  
# 
# ---
# 
# ## Example Play
# - Start: 21 sticks.  
# - Player A takes 2 → 19 left.  
# - Player B takes 3 → 16 left.  
# - Player A takes 1 → 15 left.  
# - … and so on, until one player is forced to take the last stick and loses.  
# 
# 

# In[3]:


from Game import *


# In[4]:


def number_to_english(num):
    if not 0 <= num <= 1000:
        raise ValueError("Number must be between 0 and 1000")

    if num == 0:
        return "zero"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    result = []

    # Handle thousands (only 1000)
    if num == 1000:
        return "one thousand"

    # Handle hundreds
    if num >= 100:
        result.append(ones[num // 100])
        result.append("hundred")
        num %= 100

    # Handle tens and ones
    if num >= 20:
        result.append(tens[num // 10])
        if num % 10 != 0:
            result.append(ones[num % 10])
    elif num >= 10:
        result.append(teens[num - 10])
    elif num > 0:
        result.append(ones[num])

    return " ".join(result)

def english_to_number(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    text = text.lower().strip()

    if text == "zero":
        return 0

    # Word to number mappings
    ones_map = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9
    }

    teens_map = {
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
        "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19
    }

    tens_map = {
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }

    # Split into words and process
    words = text.split()
    result = 0
    current = 0

    i = 0
    while i < len(words):
        word = words[i]

        if word == "thousand":
            result += current * 1000
            current = 0
        elif word == "hundred":
            current *= 100
        elif word in tens_map:
            current += tens_map[word]
        elif word in teens_map:
            current += teens_map[word]
        elif word in ones_map:
            current += ones_map[word]
        else:
            raise ValueError(f"Unknown word: {word}")

        i += 1

    result += current

    if result > 1000:
        raise ValueError("Result exceeds 1000")

    return result


# In[5]:


def initial_state(N=21):
    return number_to_english(N)


# In[6]:


def show_state(state,player):
    print("Player",player)
    print(f"Sticks remaining: {state}")


# In[7]:


def valid_moves(state,player):
    # return a **list** of moves that are valid

    state=english_to_number(state)

    if state==1:
        return [1]
    elif state==2:
        return [1,2]
    else:
        return [1,2,3]



# In[8]:


def update_state(state,player,move):
    state=english_to_number(state)
    new_state = state - move
    new_state=number_to_english(new_state)
    return new_state


# In[9]:


def win_status(state,player):
    # return None if the game is not over
    # return 'win' if player has won
    # return 'lose' if player has lost
    # return 'stalemate' if player has stalemate
    state=english_to_number(state)

    if player==1:
        other_player=2
    else:
        other_player=1

    if state==0:
        return 'lose'
    else:
        return None


# ## Agents

# In[10]:


def human_move(state,player):
    move = int(input("Enter your move (1, 2, or 3): "))
    while move not in valid_moves(state,player):
        print("Invalid move. Try again.")
        move = int(input("Enter your move (1, 2, or 3): "))
    return move

human_agent=Agent(human_move)


# In[11]:


def random_move(state,player):
    return random.choice(valid_moves(state,player))

random_agent=Agent(random_move)


# In[12]:


from Game.minimax import *
def minimax_move(state,player):
    values,actions = minimax_values(state,player,display=False)
    return top_choice(actions,values)
minimax_agent=Agent(minimax_move)


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


# In[21]:


skittles_agent=Agent(skittles_move)
skittles_agent.T=Table()  # starts off empty
skittles_agent.post=skittles_after
skittles_agent.learning=True


# ## Running the Game

# In[22]:


count=0
SaveTable(skittles_agent.T,f"nim table{count}.json")


# In[39]:


g=Game(N=9)
g.run(minimax_agent,skittles_agent)
count+=1
SaveTable(skittles_agent.T,f"nim table{count}.json")
skittles_agent.T


# In[ ]:





# In[40]:


def Q_move(state,player,info):
    Q=info.Q   # Q-table
    learning=info.learning
    last_state=info.last_state
    last_action=info.last_action
    α=info.α  # learning rate
    γ=info.γ  # discount factor
    ϵ=info.ϵ  # random games sometimes for exploration

    # if we haven't seen this state before, initialize it
    if state not in Q:
        actions=valid_moves(state,player)
        Q[state]=Table()
        for action in actions:
            Q[state][action]=0  # start with Q-value=0

    if learning and random.random()<ϵ:
        move=random_move(state,player)
    else:
        move=top_choice(Q[state])

    if not last_action is None:
        reward=0  # mid-game reward

        if learning:
            Q[last_state][last_action]+=α*(reward + 
                                          γ*max([Q[state][a] for a in Q[state]]) - Q[last_state][last_action])

    return move


# In[41]:


def Q_after(status,player,info):
    Q=info.Q   # Q-table
    learning=info.learning
    last_state=info.last_state
    last_action=info.last_action
    α=info.α  # learning rate
    γ=info.γ  # discount factor
    ϵ=info.ϵ  # random games sometimes for exploration


    if status=='lose':
        reward=-1
    elif status=='win':
        reward=1
    elif status=='stalemate':
        reward=0.5
    else:
        reward=0

    if learning:
        Q[last_state][last_action]+=α*(reward - Q[last_state][last_action])




# In[54]:


Q1_agent=Agent(Q_move)
Q1_agent.post=Q_after
Q1_agent.Q=Table()
Q1_agent.learning=True

Q1_agent.α=0.3  # learning rate
Q1_agent.γ=0.9  # discount factor
Q1_agent.ϵ=0.1  # random games sometimes for exploration


# In[69]:


Q2_agent=Agent(Q_move)
Q2_agent.post=Q_after
Q2_agent.Q=Table()
Q2_agent.learning=True

Q2_agent.α=0.3  # learning rate
Q2_agent.γ=0.9  # discount factor
Q2_agent.ϵ=0.1  # random games sometimes for exploration


# In[70]:


count=0
SaveTable(Q2_agent.Q,f"nim Q2_{count}.json")
Q2_agent.Q


# In[71]:


g=Game(number_of_games=100,N=9)
g.display=False
g.run(minimax_agent,Q2_agent)
count+=1
SaveTable(Q2_agent.Q,f"nim Q2_{count}.json")
Q2_agent.Q


# In[72]:


for key in Q2_agent.Q:
    inner_dict=Q2_agent.Q[key]
    print(f"{key}:")
    items = [f"{k}: {inner_dict[k]:.2f}" for k in inner_dict]
    for item in items:
        print(f"    {item}")


# In[ ]:




