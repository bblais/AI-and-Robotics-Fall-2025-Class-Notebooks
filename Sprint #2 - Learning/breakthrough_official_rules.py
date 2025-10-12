from Game import *
from Game.minimax import *
from copy import deepcopy
from tqdm.notebook import tqdm

def initial_state(N=4):
    state=Board(N,N)
    state.pieces=['.','^','v']
    
    for col in range(N):
        state[0,col]=2
        state[N-1,col]=1
        
    return state

def update_state(state,player,move):
    new_state=state
    start,end=move
    new_state[end]=player
    new_state[start]=0
    return new_state

def win_status(state,player):
    N=state.shape[0]
    
    if player==1:
        other_player=2
        goal_row=0
    else:
        other_player=1
        goal_row=N-1
        
    if not valid_moves(state,other_player):
        return 'win'
    

    for col in range(N):
        if state[goal_row,col]==player:
            return 'win'
    
chess_rules=False    
def valid_moves(state,player):
    chess_rules=False

    if chess_rules:    
        if player==1:
            return state.moves(1,'n,xne,xnw')
        else:
            return state.moves(2,'s,xse,xsw')

    else:
        if player==1:
            return state.moves(1,'n,ne,nw,xne,xnw')
        else:
            return state.moves(2,'s,se,sw,xse,xsw')
        
    
    return moves

def show_state(state,player):
    print(state)


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
        
