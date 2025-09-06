#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=5  # integer
b=5.4 # floating point
c="Hello" # string


# ## Lists

# - List is a collection which is ordered and changeable. Allows duplicate members.

# In[6]:


L=[1, 2.2, "Hello", 5, "World"]


# In[7]:


L


# In[8]:


L[0] # first element


# In[9]:


L[3] # fourth element


# In[10]:


len(L)


# In[11]:


L[1]='something here' # change second element


# In[12]:


L


# In[13]:


L.append("another thing")


# In[14]:


L


# In[15]:


L.append(100)


# In[16]:


L


# In[18]:


for item in L:
    print("Item",item)


# In[19]:


for i in range(len(L)):
    print("Item",i,L[i])


# ## Boards

# In[2]:


from Game import *


# In[3]:


Board(3,3)


# In[4]:


board=Board(3,3)


# In[5]:


board.show_locations()


# In[6]:


board[3]=2


# In[7]:


board[5]=1


# In[8]:


board


# In[11]:


location=5
if board[location]==0:
    print("Empty")
else:
    print("Location already taken")


# In[13]:


for location in range(9):
    if board[location]==0:
        print("Location",location,"is empty")
    else:
        print("Location",location,"is taken by player",board[location])


# In[14]:


# make a list of all of the empty locations
empty_locations=[]
for location in range(9):
    if board[location]==0:
        empty_locations.append(location)
    else:
        pass



# In[15]:


empty_locations


# In[16]:


board[0]=1


# In[17]:


# make a list of all of the empty locations
empty_locations=[]
for location in range(9):
    if board[location]==0:
        empty_locations.append(location)
    else:
        pass



# In[18]:


empty_locations


# In[19]:


board=Board(5,5)
board


# In[20]:


board.show_locations()


# In[23]:


board=Board(5,5)
#board.pieces=['.','X','O']  # optional
board[1]=1
board[3]=1
board[5]=1
board[7]=1
board[9]=1
print(board)


# In[25]:


board=Board(5,5)
#board.pieces=['.','X','O']  # optional

for location in [1,3,5,7,9]:
    board[location]=1

for location in [15,17,19,21,23]:
    board[location]=2

print(board)


# In[ ]:




