#!/usr/bin/env python
# coding: utf-8

# - Nim
# - Tic Tac Toe - TTT
# - Checkers

# ## State
# 
# - Everything that specified the current situation of the game. (e.g., board configuration, current player, etc.)
# 
# ## Move
# 
# - Way of specifying a player's action. (e.g., removing sticks, placing symbols, moving pieces, etc.)

# In[ ]:





# In[ ]:





# ## Nim
# 
# - Start with some number of sticks (e.g., 21).
# - Players take turns removing 1, 2, or 3 sticks.
# - The player who takes the last stick loses.
# 
# Example:
# 
# - Initial sticks: 21
# - Player 1 takes 3 sticks (remaining: 18)
# - Player 2 takes 2 sticks (remaining: 16)
# - Player 1 takes 1 stick (remaining: 15)
# - Player 2 takes 3 sticks (remaining: 12)
# - Player 1 takes 2 sticks (remaining: 10)
# - Player 2 takes 1 stick (remaining: 9)
# - Player 1 takes 3 sticks (remaining: 6)
# - Player 2 takes 2 sticks (remaining: 4)
# - Player 1 takes 1 stick (remaining: 3)
# - Player 2 takes 2 sticks (remaining: 1) --> Player 1 loses

# - State = number of remaining sticks. (integer)
# - Move = number of sticks to remove (integer)
# - A single valid move in Nim is a number from 1, 2, or 3 (provided that the number of remaining sticks is greater than or equal to the number of sticks being removed.)

# In[ ]:





# ### Tic Tac Toe (TTT)
# 
# - Played on a 3x3 grid.
# - Players take turns placing their symbol (X or O) in an empty cell.
# - The first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins.

# - State = 3x3 grid (Board from Game library) with values 0, 1 or 2 (0 = empty, 1 = X, 2 = O)
# - move = location (integer)
# - single valid move in TTT is an integer from 0 to 8 (representing the locations of the 9 cells in the grid) - provided that the board[move]==0 (empty)

# In[ ]:





# ## Checkers

# - State is an 8x8 grid (Board from Game library) with values 0, 1, 2, 3 or 4 (0 = empty, 1 = player 1's piece, 2 = player 2's piece, 3 = player 1's king, 4 = player 2's king)
# - Move is small length-2 list of [start location, end location] (both integers) (e.g. [12, 16] means move piece from location 12 to location 16)
# - Single valid move in Checkers is a length-2 list of integers [start, end] where:
#   - start and end are both integers from 0 to 63 (representing the locations of the 64 cells in the 8x8 grid)
#   - board[start] is either 1 or 3 if it's player 1's turn, or either 2 or 4 if it's player 2's turn (indicating that the piece being moved belongs to the current player)
#   - The move follows the rules of Checkers (e.g., moving diagonally, capturing opponent's pieces, etc.)
#   - board[end] == 0 (indicating that the destination cell is empty)

# ## Game Library
# 
# - initial_state: function that returns the initial state of the game.
# - valid_moves: function that takes a state and a player and returns a **list** of every single valid move for that state.
# - update_state: function that takes a state, a move, and a player and returns the new state after applying the move.
# - win_status: function that takes a state and player returns:
#   - None if the game is ongoing,
#   - 'win' if player has won,
#   - 'lose' if player has lost,
#   - 'stalemate' if the game is a draw.
# - show_state: function that takes a state and prints it in a human-readable format.

# ### Nim

# - initial_state: return 21 (or any other starting number of sticks).
# - valid_moves: return [1, 2, 3] 
# - update_state: new_state=state-move ;  return new_state
# - win_status: check if the state is 0 (current player loses), otherwise None.
#   - None if the game is ongoing,
#   - 'win' if player has won,
#   - 'lose' if player has lost,
#   - 'stalemate' if the game is a draw.
# - show_state: print(state)

# ### Tic Tac Toe (TTT)

# - initial_state: state=Board(3,3) return state
# - valid_moves: moves=[];  loop through board, if board[locations]==0 then moves.append(location).  e.g. [1,4,5,6,8] 
# - update_state: new_state=state;  new_state[move]=player ;  return new_state
# - win_status: run through all the winning combinations, if any is filled with player's symbol then 'win', if any is filled with opponent's symbol then 'lose', if no empty cells left then 'stalemate', else None.
#   - None if the game is ongoing,
#   - 'win' if player has won,
#   - 'lose' if player has lost,
#   - 'stalemate' if the game is a draw.
# - show_state: print(state)

# ### Checkers

# - initial_state: state=Board(8,8); go through certain locations board[location]=1 or board[location]=2; return state
# - valid_moves: moves=[];  loop through board, if board[location]==player; check for various move directions for all end points,  then moves.append([start,end]).  e.g. [ [3,5], [3,7], [10,12], ] 
# - update_state: new_state=state; start,end=move new_state[start]=0  new_state[end]=player ;  return new_state
# - win_status: if not(valid_moves(state,other_player)) return 'win',if one player has no pieces left or no valid moves, they lose; if both players have pieces and valid moves, None; if neither player can move, 'stalemate'.
#   - None if the game is ongoing,
#   - 'win' if player has won,
#   - 'lose' if player has lost,
#   - 'stalemate' if the game is a draw.
# - show_state: print(state)

# In[1]:


start=5
end=3

move=[start,end]

moves=[]
moves.append(move)

moves


# In[ ]:




