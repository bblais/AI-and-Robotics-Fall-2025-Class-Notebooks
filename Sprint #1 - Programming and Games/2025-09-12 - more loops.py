#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mplturtle import *


# ![image.png](attachment:0e05fa38-552c-4b11-babb-6470ed11e8b0.png)

# In[2]:


def square(size):
    for i in range(4):
        forward(size)
        right(90)


# In[3]:


reset()

square(100)
forward(100)

square(100)
forward(100)

square(100)
forward(100)


# In[4]:


reset()

for i in range(12):
    square(100)
    forward(100)


# In[5]:


reset()

for i in range(12):
    square(100)
    forward(100)

right(180)
forward(100*11)
right(90)

for i in range(11):
    square(100)
    forward(100)


# In[7]:


reset()

for i in range(12):
    square(100)
    forward(100)

right(180)
forward(100*11)
right(90)
forward(100)
right(90)

for i in range(11):
    square(100)
    forward(100)


# In[8]:


reset()

for i in range(12):
    square(100)
    forward(100)

right(180)
forward(100*11+50)
right(90)
forward(100)
right(90)

for i in range(11):
    square(100)
    forward(100)


# In[10]:


reset()

number_of_squares = 12

for j in range(12):
    for i in range(number_of_squares):
        square(100)
        forward(100)

    number_of_squares=number_of_squares-1
    right(180)
    forward(100*number_of_squares+50)
    right(90)
    forward(100)
    right(90)


# In[11]:


reset()

number_of_squares = 12

for j in range(12):
    for i in range(number_of_squares):
        square(100)
        forward(100)

    number_of_squares=number_of_squares-1

    penup()
    right(180)
    forward(100*number_of_squares+50)
    right(90)
    forward(100)
    right(90)
    pendown()


# In[ ]:





# ![image.png](attachment:efb547fc-b60a-4319-bdd9-8fd8d01c6bfe.png)

# In[18]:


reset()

size=150
pencolor("red")
for i in range(50):
    circle(size)
    right(10)
    size=size+2


size=100

pencolor("orange")
for i in range(50):
    circle(size)
    right(10)
    size=size+2



# close, but not quite.

# In[24]:


from numpy import cos,sin,radians


# In[27]:


reset()

size=100
for angle in range(0,360,10):
    x,y=30*cos(radians(angle)),30*sin(radians(angle))
    penup()
    goto(x,y)
    pendown()
    circle(size)
    size-=1


# In[ ]:




