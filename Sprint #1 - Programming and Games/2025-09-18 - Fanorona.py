#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# # Fanorona (5×5 Variant)
# 
# ## Board
# - A **5×5 grid** of points.  
# - Lines connect **horizontally, vertically, and diagonally** (like king moves in chess).  
# - There are 25 intersections in total.  
# 
# ---
# 
# ## Setup
# - Two players, each with **12 stones** (● and ○).  
# - Stones are placed on all points **except the center (12)**.  
# - Traditionally:  
#   - Top 2 rows = Player A’s stones.  
#   - Bottom 2 rows = Player B’s stones.  
#   - Middle row = split, with the center left empty.  
# 
# Example starting position:  
# ```
# ● ● ● ● ●
# ● ● ● ● ●
# ● ● ⊙ ○ ○
# ○ ○ ○ ○ ○
# ○ ○ ○ ○ ○
# ```
# 
# (⊙ = empty center)
# 
# ---
# 
# ## Moves
# 1. A piece may **move one step** along a connecting line into an adjacent empty point.  
# 2. **Capturing happens in two ways:**  
#    - **Approach capture**: If you move **toward** a line of adjacent enemy pieces, all contiguous enemies in that line are captured.  
#    - **Withdrawal capture**: If you move **away** from a line of adjacent enemy pieces, those enemies are captured.  
# 3. **Multiple captures**: After a capture, the same piece may continue capturing, provided it does not revisit the same point in the sequence.  
# 4. A move can switch between **approach** and **withdrawal** captures in the same sequence.  
# 
# ---
# 
# ## Goal
# - Win by **capturing all opponent pieces**.  
# - If neither player can force progress, the game is a draw.  
# 
# ---
# 
# ## Capture Examples
# 
# ### Example 1 — Approach Capture
# ```
# ● ⊙ ○ ○ ○
# ```
# - ● moves **right into ⊙**.  
# - This is **toward** the line of ○’s.  
# - Result: the three ○’s are captured.  
# 
# Resulting board:  
# ```
# ● ● ⊙ ⊙ ⊙
# ```
# 
# ---
# 
# ### Example 2 — Withdrawal Capture
# ```
# ○ ○ ○ ● ⊙
# ```
# - ● moves **right into ⊙**.  
# - This is **away** from the contiguous ○’s to the left.  
# - Result: the three ○’s are captured.  
# 
# Resulting board:  
# ```
# ⊙ ⊙ ⊙ ⊙ ●
# ```
# 
# ---
# 
# ### Example 3 — Combined Example
# ```
# ● ○ ○ ○ ● ⊙
# ```
# Positions labeled:  
# ```
# [0] ●   [1] ○   [2] ○   [3] ○   [4] ●   [5] ⊙
# ```
# 
# - The right-hand ● at [4] moves into [5].  
# - This is a **withdrawal** from the three contiguous ○’s at [1], [2], [3].  
# - All three ○’s are captured.  
# 
# Resulting board:  
# ```
# ● ⊙ ⊙ ⊙ ⊙ ●
# ```
# 
# ---
# 
# ## Why It’s Fun
# - The 5×5 version plays quickly (10–15 minutes).  
# - **Captures can chain dramatically**, creating big swings.  
# - The tension between **approach** and **withdrawal** makes every move strategic.  
# 

# # Instructions for AI
# 
# I am implementing Fanorona with a particular game library.  It has a Board class that can be indexed by location, like:
# 
# 
#     state=Board(5,5)
#     state[0]=1   # index with location
#     state[1,2]=2  # index with row and column, both 0-indexed
# 
# 
#      1  0  0  0  0 
#      0  0  2  0  0 
#      0  0  0  0  0 
#      0  0  0  0  0 
#      0  0  0  0  0 
# 
# The library expects 5 functions, which we will implement in turn.  First is initial_state which takes no arguments and returns the initial state.  Please write the initial_state function for Fanorona.
# 
# I prefer to write functions in terms in single-integer locations whereever possible.  the Board defaults to 0's so you don't need to do that.  please write the functions using single-integer locations instead of row and column where possible.  Where it makes sense to use row and column, there are methods of the Board class to convert, so you don't need divmod.  for example
# 
#     location=5
#     state.col(location)  # returns the column for the location
#     state.row(location)  # returns the row for the location
# 
# the next function is show_state which takes state and player and prints out the current board.  the Board class can also do this:
# 
#     state.pieces=['.','O','X']
# 
# which sets the display of the pieces when printing out the state.  add this to initial_state and write the show_state function.
# 
# A move will be a length-2 list of start and end locations for a piece.  the valid_moves function takes a state and a player and returns a list of all of the valid moves for that player.  Please write this function and I'll give feedback on it when I see it.
# 
# I don't like nested loops.  make a neighbors function to return all of the single-integer neighbors of a given location, and rewrite the valid_moves function. 
# 
# the function update_state takes a state, player, and a move and returns a new_state with the pieces updated. please write this and I'll give feedback..  update state has to include the capture and withdrawel as well.
# 
# the function win_status takes a state (after the update state is called), the player (that made the last move) and returns 'win' if this updated state is a winning state for that player, 'lose' if it is a losing state, 'stalemate' for a stalemate, or None otherwise (just a mid-game state).  since this state will not be given a move by the current player, the my_moves is not relevant. 
# 
# 
# now I want a heuristic function which takes a state and player and returns a number between -1 and 1 for the value of the state based off of a heuristic like material advantage. clamp to -0.99 and +0.99 because it won't be a perfect measure. 

# # Game Functions

# In[2]:


def initial_state():
    """
    Return the starting Board for Fanorona (5x5 variant).

    Convention:
      0 = empty (.)
      1 = player 1 (O)
      2 = player 2 (X)
    """
    state = Board(5, 5)
    state.pieces = ['.', 'O', 'X']

    # Top two rows (indices 0–9): player 1
    for i in range(0, 10):
        state[i] = 1

    # Middle row (indices 10–14): 1, 1, 0, 2, 2
    state[10] = 1
    state[11] = 1
    state[12] = 0  # center empty
    state[13] = 2
    state[14] = 2

    # Bottom two rows (indices 15–24): player 2
    for i in range(15, 25):
        state[i] = 2

    return state


def show_state(state, player):
    """
    Print the current board state.
    `player` argument is unused for display but included for consistency.
    """
    print(state)



# In[3]:


def neighbors(state, loc):
    """
    Return a list of single-integer neighbor locations (king moves) for `loc`.
    Uses the board's row/col helpers; computes indices in row-major order.
    """
    rows, cols = 5, 5  # or: getattr(state, "rows", 5), getattr(state, "cols", 5)
    r, c = state.row(loc), state.col(loc)
    out = []

    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                out.append(nr * cols + nc)  # single-integer location

    return out


def valid_moves(state, player):
    """
    Return all single-step moves [start, end] for `player` into empty neighbors.
    (This is the movement skeleton; capture sequences will be layered on later.)
    """
    moves = []
    total = 25  # 5x5

    for start in range(total):
        if state[start] != player:
            continue
        for end in neighbors(state, start):
            if state[end] == 0:
                moves.append([start, end])

    return moves


# In[4]:


def update_state(state, player, move):
    """
    Apply a single-step Fanorona move [start, end] for `player` and return a new Board.
    Captures:
      - Approach capture: moving TOWARD a contiguous line of enemy pieces removes them.
      - Withdrawal capture: moving AWAY from a contiguous line of enemy pieces removes them.
    If both are available on the same step, this implementation chooses APPROACH by default.

    Assumes:
      - Players are 1 and 2.
      - `move` is a legal one-step move (adjacent end and empty).
      - Multi-capture chaining is handled by the caller via multiple calls if desired.
    """
    start, end = move
    opponent = 3 - player

    # Copy state so we return a new board
    new_state = state

    # Movement direction (dr, dc) from start -> end
    rs, cs = state.row(start), state.col(start)
    re, ce = state.row(end), state.col(end)
    dr = re - rs
    dc = ce - cs

    # Helper: collect contiguous opponent stones starting from (r0, c0) stepping (dr, dc)
    def collect_ray(r0, c0, dr, dc):
        captures = []
        r, c = r0 + dr, c0 + dc
        while 0 <= r < 5 and 0 <= c < 5:
            idx = r * 5 + c
            if new_state[idx] == opponent:
                captures.append(idx)
                r += dr
                c += dc
            else:
                break
        return captures

    # Approach: from END, look forward along (dr, dc)
    approach_caps = collect_ray(re, ce, dr, dc)

    # Withdrawal: from START, look backward along (-dr, -dc)
    withdrawal_caps = collect_ray(rs, cs, -dr, -dc)

    # Decide which capture to perform (if any)
    if approach_caps and withdrawal_caps:
        chosen_caps = approach_caps   # default to approach if both available
    elif approach_caps:
        chosen_caps = approach_caps
    elif withdrawal_caps:
        chosen_caps = withdrawal_caps
    else:
        chosen_caps = []

    # Execute the move
    new_state[end] = player
    new_state[start] = 0

    # Remove captured stones
    for idx in chosen_caps:
        new_state[idx] = 0

    return new_state


# In[5]:


def win_status(state, player):
    """
    Given the state AFTER `player` just moved, return:
      - 'win'       if the opponent has no pieces or no legal moves
      - 'lose'      if player has no pieces (safety check)
      - 'stalemate' if both players have no pieces (extremely rare)
      - None        otherwise (game continues)
    """
    opponent = 3 - player
    total = 25  # 5x5 board

    # Count pieces
    p_count = sum(1 for i in range(total) if state[i] == player)
    o_count = sum(1 for i in range(total) if state[i] == opponent)

    if o_count == 0 and p_count > 0:
        return 'win'
    if p_count == 0 and o_count > 0:
        return 'lose'
    if o_count == 0 and p_count == 0:
        return 'stalemate'

    # Check opponent mobility
    opp_moves = valid_moves(state, opponent)
    if not opp_moves:
        return 'win'

    return None


# # Agents

# In[6]:


def human_move(state,player):
    state.show_locations()
    moves=valid_moves(state,player)
    print("Valid moves are: ",moves)
    move=None
    while move not in moves:
        move_input=input("Enter your move as start,end: ")
        start,end=move_input.split(",")
        move=[int(start),int(end)]

    return move

human_agent=Agent(human_move) 


# In[7]:


def random_move(state,player):
    return random.choice(valid_moves(state,player))
random_agent=Agent(random_move)    


# In[8]:


from Game.minimax import *
def minimax_move(state,player):
    values,actions = minimax_values(state,player,display=False,maxdepth=2)
    return top_choice(actions,values)
minimax_agent=Agent(minimax_move)


# # Playing the Game

# In[9]:


# g=Game()
# g.run(human_agent,random_agent)


# ### Sample Game
# 
#     ====
#     Game  1
#      O  O  O  O  O 
#      O  O  O  O  O 
#      O  O  .  X  X 
#      X  X  X  X  X 
#      X  X  X  X  X 
#     
#      0  1  2  3  4 
#      5  6  7  8  9 
#     10 11 12 13 14 
#     15 16 17 18 19 
#     20 21 22 23 24 
#     
#     Valid moves are:  [[6, 12], [7, 12], [8, 12], [11, 12]]
#     Enter your move as start,end:  7,12
#     Player 1 moves [7, 12]
#      O  O  O  O  O 
#      O  O  .  O  O 
#      O  O  O  X  X 
#      X  X  .  X  X 
#      X  X  .  X  X 
#     
#     Player 2 moves [18, 17]
#      O  O  O  O  O 
#      O  O  .  O  O 
#      O  O  O  X  X 
#      X  X  X  .  X 
#      X  X  .  X  X 
#     
#      0  1  2  3  4 
#      5  6  7  8  9 
#     10 11 12 13 14 
#     15 16 17 18 19 
#     20 21 22 23 24 
#     
#     Valid moves are:  [[1, 7], [2, 7], [3, 7], [6, 7], [8, 7], [11, 7], [12, 7], [12, 18]]
#     Enter your move as start,end:  12,18
#     Player 1 moves [12, 18]
#      O  O  O  O  O 
#      O  O  .  O  O 
#      O  O  .  X  X 
#      X  X  X  O  X 
#      X  X  .  X  . 
#     
#     Player 2 moves [16, 12]
#      O  O  O  O  . 
#      O  O  .  .  O 
#      O  O  X  X  X 
#      X  .  X  O  X 
#      X  X  .  X  . 
#     
#      0  1  2  3  4 
#      5  6  7  8  9 
#     10 11 12 13 14 
#     15 16 17 18 19 
#     20 21 22 23 24 
#     
#     Valid moves are:  [[1, 7], [2, 7], [2, 8], [3, 4], [3, 7], [3, 8], [6, 7], [9, 4], [9, 8], [10, 16], [11, 7], [11, 16], [18, 22], [18, 24]]
#     Enter your move as start,end:  2,7
#     Player 1 moves [2, 7]
#      O  O  .  O  . 
#      O  O  O  .  O 
#      O  O  .  X  X 
#      X  .  .  O  X 
#      X  X  .  X  . 
#     
#     Player 2 moves [23, 17]
#      O  O  .  O  . 
#      .  O  O  .  O 
#      O  .  .  X  X 
#      X  .  X  O  X 
#      X  X  .  .  . 
#     
#      0  1  2  3  4 
#      5  6  7  8  9 
#     10 11 12 13 14 
#     15 16 17 18 19 
#     20 21 22 23 24 
#     
#     Valid moves are:  [[0, 5], [1, 2], [1, 5], [3, 2], [3, 4], [3, 8], [6, 2], [6, 5], [6, 11], [6, 12], [7, 2], [7, 8], [7, 11], [7, 12], [9, 4], [9, 8], [10, 5], [10, 11], [10, 16], [18, 12], [18, 22], [18, 23], [18, 24]]
#     Enter your move as start,end:  9,4
#     Player 1 moves [9, 4]
#      O  O  .  O  O 
#      .  O  O  .  . 
#      O  .  .  X  . 
#      X  .  X  O  . 
#      X  X  .  .  . 
#     
#     Player 2 moves [13, 19]
#      O  .  .  O  O 
#      .  O  .  .  . 
#      O  .  .  .  . 
#      X  .  X  O  X 
#      X  X  .  .  . 
#     
#      0  1  2  3  4 
#      5  6  7  8  9 
#     10 11 12 13 14 
#     15 16 17 18 19 
#     20 21 22 23 24 
#     
#     Valid moves are:  [[0, 1], [0, 5], [3, 2], [3, 7], [3, 8], [3, 9], [4, 8], [4, 9], [6, 1], [6, 2], [6, 5], [6, 7], [6, 11], [6, 12], [10, 5], [10, 11], [10, 16], [18, 12], [18, 13], [18, 14], [18, 22], [18, 23], [18, 24]]
#     Enter your move as start,end:  10,5
#     Player 1 moves [10, 5]
#      O  .  .  O  O 
#      O  O  .  .  . 
#      .  .  .  .  . 
#      .  .  X  O  X 
#      .  X  .  .  . 
#     
#     Player 2 moves [17, 16]
#      O  .  .  O  O 
#      O  O  .  .  . 
#      .  .  .  .  . 
#      .  X  .  .  X 
#      .  X  .  .  . 
#     
#      0  1  2  3  4 
#      5  6  7  8  9 
#     10 11 12 13 14 
#     15 16 17 18 19 
#     20 21 22 23 24 
#     
#     Valid moves are:  [[0, 1], [3, 2], [3, 7], [3, 8], [3, 9], [4, 8], [4, 9], [5, 1], [5, 10], [5, 11], [6, 1], [6, 2], [6, 7], [6, 10], [6, 11], [6, 12]]
#     Enter your move as start,end:  6,11
#     Player 1 moves [6, 11]
#      O  .  .  O  O 
#      O  .  .  .  . 
#      .  O  .  .  . 
#      .  .  .  .  X 
#      .  .  .  .  . 
#     
#     Player 2 moves [19, 14]
#      O  .  .  O  O 
#      O  .  .  .  . 
#      .  O  .  .  X 
#      .  .  .  .  . 
#      .  .  .  .  . 
#     
#      0  1  2  3  4 
#      5  6  7  8  9 
#     10 11 12 13 14 
#     15 16 17 18 19 
#     20 21 22 23 24 
#     
#     Valid moves are:  [[0, 1], [0, 6], [3, 2], [3, 7], [3, 8], [3, 9], [4, 8], [4, 9], [5, 1], [5, 6], [5, 10], [11, 6], [11, 7], [11, 10], [11, 12], [11, 15], [11, 16], [11, 17]]
#     Enter your move as start,end:  4,9
#     Player 1 moves [4, 9]
#      O  .  .  O  . 
#      O  .  .  .  O 
#      .  O  .  .  . 
#      .  .  .  .  . 
#      .  .  .  .  . 
#     
#     Player  1 won.
#     [1]

# Which is better?
# 
# 1. 
# 
# 
#      O  .  .  O  O 
#      .  .  O  .  . 
#      O  X  .  .  . 
#      X  X  X  O  X 
#      X  X  .  .  . 
# 
# 2.
# 
#      O  O  .  O  O 
#      .  .  .  .  . 
#      O  .  .  .  . 
#      X  .  X  O  X 
#      X  .  .  .  . 
#      
# 

# In[10]:


def material(state, player):
    """
    Normalized material advantage in [-1, 1].
    """
    opponent = 3 - player

    my_pieces = 0
    opp_pieces = 0
    i = 0
    for i in range(25):
        if state[i] == player:
            my_pieces += 1
        elif state[i] == opponent:
            opp_pieces += 1
        else:
            pass

    denom = my_pieces + opp_pieces
    if denom == 0:
        value = 0.0
    else:
        value = (my_pieces - opp_pieces) / denom

    return value


def mobility(state, player):
    """
    Normalized mobility advantage in [-1, 1] using valid_moves.
    """
    opponent = 3 - player

    my_moves = len(valid_moves(state, player))
    opp_moves = len(valid_moves(state, opponent))

    denom = my_moves + opp_moves
    if denom == 0:
        value = 0.0
    else:
        value = (my_moves - opp_moves) / denom

    return value


def center_control(state, player):
    """
    Small bonus/penalty for owning the center.
    +0.05 if player holds center, -0.05 if opponent holds center, 0 otherwise.
    """
    opponent = 3 - player

    if state[12] == player:
        bonus = 0.05
    elif state[12] == opponent:
        bonus = -0.05
    else:
        bonus = 0.0

    return bonus








# In[11]:


def heuristic(state, player):
    """
    Combine material, mobility, and center control into [-0.99, 0.99].
    Weights: 0.7 * material + 0.3 * mobility + center_control
    """

    if player==1:
        return 0

    mat = material(state, player)
    mob = mobility(state, player)
    ctr = center_control(state, player)

    score = 0.7 * mat + 0.3 * mob + ctr

    if score > 0.99:
        score = 0.99
    elif score < -0.99:
        score = -0.99

    return score


# In[ ]:





# In[ ]:





# In[12]:


get_ipython().run_cell_magic('time', '', 'g=Game(number_of_games=10)\ng.display=False\ng.check_repeated_states=True  # you lose if you give your opponent a repeated state\nresult=g.run(minimax_agent,minimax_agent)\nprint(result)\n')


# In[ ]:




