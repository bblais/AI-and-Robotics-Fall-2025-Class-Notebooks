from Game import *

def initial_state():
    state=Board(4,4)

    N=prod(state.shape)

    state[0]=1
    state[1]=0
    state[2]=0
    state[3]=1
    state[5]=1

    state[12]=2
    state[13]=2
    state[14]=2
    state[15]=2

    return state



