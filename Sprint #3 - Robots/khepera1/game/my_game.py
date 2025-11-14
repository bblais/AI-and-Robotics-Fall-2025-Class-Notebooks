from Game import *

def initial_state():
    state=Board(5,5)

    N=prod(state.shape)

    for i in range(N//2):
        state[i]=1
        
    for i in range(N//2,N):
        state[i]=2    
    return state

