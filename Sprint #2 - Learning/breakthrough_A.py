from Game import *
from Game.minimax import *
from copy import deepcopy
from tqdm.notebook import tqdm

def initial_state(N=None):
    state = Board(4,4)
    for location in range(4):
        state[location] = 2
    for location in range(12, 16):
        state[location] = 1
    state.pieces = ['.', chr(9679), chr(9675)]
    return state

def update_state(state, player, move):
    start, end = move
    newState = state
    newState[start] = 0
    newState[end] = player
    return newState

def win_status(state, player):
    if player == 1:
        for location in range(4):
            if state[location] == 1:
                return 'win'
        for location in range(12, 16):
            if state[location] == 2:
                return 'loss'
        if not valid_moves(state, 2):
            return 'win'
    elif player == 2:
        for location in range(4):
            if state[location] == 1:
                return 'loss'
        for location in range(12, 16):
            if state[location] == 2:
                return 'win'
        if not valid_moves(state, 1):
            return 'win'

            
def forward_squares(location, player):
    # player 2
    if location == 0 and player == 2:
        return [4,5]
    if location == 1 and player == 2:
        return [4, 5, 6]
    if location == 2 and player == 2:
        return [5, 6, 7]
    if location == 3 and player == 2:
        return [6, 7]
    if location == 4 and player == 2:
        return [8,9]
    if location == 5  and player == 2:
        return [8, 9, 10]
    if location == 6 and player == 2:
        return [9,10,11]
    if location == 7 and player == 2:
        return [10,11]
    if location == 8 and player == 2:
        return [12, 13]
    if location ==9 and player ==2:
        return [12, 13, 14]
    if location == 10 and player == 2:
        return [13, 14, 15]
    if location == 11 and player == 2:
        return [14,15]
    # player 1
    if location == 4 and player == 1:
        return [0,1]
    if location == 5  and player == 1:
        return [0, 1, 2]
    if location == 6 and player == 1:
        return [1, 2, 3]
    if location == 7 and player == 1:
        return [2, 3]
    if location == 8 and player == 1:
        return [4, 5]
    if location ==9 and player ==1:
        return [4, 5, 6]
    if location == 10 and player == 1:
        return [5, 6, 7]
    if location == 11 and player == 1:
        return [6, 7]
    if location == 12 and player ==1:
        return [8,9]
    if location == 13 and player == 1:
        return [8, 9, 10]
    if location == 14 and player == 1:
        return [9, 10, 11]
    if location == 15 and player == 1:
        return [10,11]

def diagonal_squares(location, player):
        # player 2
    if location == 0 and player == 2:
        return [5]
    if location == 1 and player == 2:
        return [4, 6]
    if location == 2 and player == 2:
        return [5, 7]
    if location == 3 and player == 2:
        return [6]
    if location == 4 and player == 2:
        return [9]
    if location == 5  and player == 2:
        return [8, 10]
    if location == 6 and player == 2:
        return [9, 11]
    if location == 7 and player == 2:
        return [10]
    if location == 8 and player == 2:
        return [13]
    if location ==9 and player ==2:
        return [12, 14]
    if location == 10 and player == 2:
        return [13, 15]
    if location == 11 and player == 2:
        return [14]
    # player 1
    if location == 4 and player == 1:
        return [1]
    if location == 5  and player == 1:
        return [0, 2]
    if location == 6 and player == 1:
        return [1, 3]
    if location == 7 and player == 1:
        return [2]
    if location == 8 and player == 1:
        return [5]
    if location ==9 and player ==1:
        return [4, 6]
    if location == 10 and player == 1:
        return [5, 7]
    if location == 11 and player == 1:
        return [6]
    if location == 12 and player ==1:
        return [9]
    if location == 13 and player == 1:
        return [8, 10]
    if location == 14 and player == 1:
        return [9, 11]
    if location == 15 and player == 1:
        return [10]
        
def valid_moves(state, player):
    if player == 1:
        otherPlayer = 2
    else:
        otherPlayer = 1

    moves = []
    for start in range(16):
        if state[start] != player:
            continue
        for end in range(16):
            if state[end] == 0 and end in forward_squares(start, player):
                move = [start, end]
                moves.append(move)
            if state[end] == otherPlayer and end in diagonal_squares(start, player):
                move = [start, end]
                moves.append(move)
                
    return moves

    
def show_state(state, player):
    print("Waiting on Player", player)
    print(state)
    print(state.show_locations())

def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)


def human_move(state,player):

    moves=valid_moves(state,player)
    print("Locations:")
    state.show_locations()
    
    print( "Player ", player)
    print("Moves:")
    for i, move in enumerate(moves):
        print(f"\t{i}: {move}")
        
    valid_move=False
    while not valid_move:
        move_number=int(input('Which move do you want (enter a number)?'))

        if move_number in range(len(moves)):
            valid_move=True
        else:
            print( "Illegal move.")

    
    return moves[move_number]




human_agent=Agent(human_move)
random_agent=Agent(random_move)

def minimax_move(state,player,info):

    T=info.T
    
    if not state in T:
        values,moves=minimax_values(state,player,display=False)
        move=top_choice(moves,values)
        T[state]=move
    else:    
        move=T[state]
        
    return move


minimax_agent=Agent(minimax_move)
minimax_agent.T=Table()

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



def Q_move(state,player,info):
    Q=info.Q
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    
    α=info.α  # learning rate
    ϵ=info.ϵ  # how often to take a random move
    γ=info.γ  # memory constant -- how quickly does the table update back in time (earlier in the game)
    
    # \alpha <hit tab>    α
    # \epsilon <hit tab>  ϵ
    # \gamma <hit tab>    γ
    
    if state not in Q:
        actions=valid_moves(state,player)
        Q[state]=Table()
        for action in actions:
            Q[state][action]=0  # initial value of table
    
    if learning:
        if random.random()<ϵ:  # take a random move occasionally to explore the environment
            move=random_move(state,player)
        else:
            move=top_choice(Q[state])
    else:
        move=top_choice(Q[state])
    
    if not last_action is None:  # not the first move
        reward=0
        
        # learn
        if learning:
            Q[last_state][last_action]+=α*(reward +
                        γ*max([Q[state][a] for a in Q[state]]) - Q[last_state][last_action])
    
    return move

def Q_after(status,player,info):
    Q=info.Q
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    
    α=info.α  # learning rate
    ϵ=info.ϵ  # how often to take a random move
    γ=info.γ  # memory constant -- how quickly does the table update back in time (earlier in the game)
    
    # \alpha <hit tab>    α
    # \epsilon <hit tab>  ϵ
    # \gamma <hit tab>    γ

    if status=='lose':
        reward=-1
    elif status=='win':
        reward=1
    elif status=='stalemate':
        reward=.5 # value stalemate a little closer to a win
    else:
        reward=0
    
    
    if learning:
        Q[last_state][last_action]+=α*(reward - Q[last_state][last_action])
        
