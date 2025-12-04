from Game import *

def initial_state(N=4):
    state=Board(N,N)

    #state.pieces=['.','^','v']
    
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
    
chess_rules=True    
def valid_moves(state,player):
    chess_rules=True

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

