#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle
t = turtle.Turtle()
for i in range(4):
    t.forward(60)
    t.right(90)
t.penup()
t.forward(30)
t.pendown()
t.left(45)
t.forward(42)


# In[3]:


from mplturtle import *


# In[4]:


reset()
for i in range(4):
    forward(60)
    right(45)
penup()
forward(30)
pendown()
left(45)
forward(42)


# In[5]:


from Game import *


# In[7]:


state=Board(3,3)
state.pieces=['.','X','O']
state.board=[1,2,0,2,1,0,0,0,1]
print(state)


# In[9]:


T=Table()
T[state]=Table()
for action,value in zip([2, 5, 6, 7],[3,2,4,1]):
    T[state][action]=value


# In[11]:


print(T)


# In[ ]:




