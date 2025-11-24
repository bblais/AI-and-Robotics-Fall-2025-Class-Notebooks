player=1
im=take_picture()

state=read_state(im)

move=get_move(state,player)

make_move(move)
