#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mplturtle import *


# In[2]:


def square(size):
    for i in range(4):
        forward(size)
        right(90)


# In[3]:


reset()
square(100)


# In[6]:


def somefunction(size,shape):

    if shape=="square":
        square(size)


# In[7]:


reset()
somefunction(100,"square")


# In[16]:


from random import random,randint,choice


# In[11]:


random()


# In[15]:


reset()

penup()
goto( (random()*2-1)*100, (random()*2-1)*100 )
pendown()

square(20)

penup()
goto( (random()*2-1)*100, (random()*2-1)*100 )
pendown()

square(20)


# In[19]:


reset()

penup()
goto( randint(-100,100), randint(-100,100))
pendown()

pencolor(choice(["red","green","blue","black","orange","purple"]))
square(20)

penup()
goto( randint(-100,100), randint(-100,100))
pendown()

pencolor(choice(["red","green","blue","black","orange","purple"]))
square(20)


# In[ ]:




