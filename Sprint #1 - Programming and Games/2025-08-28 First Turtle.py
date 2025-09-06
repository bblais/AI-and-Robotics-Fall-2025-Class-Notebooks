#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mplturtle import *


# In[2]:


reset()
forward(50)
right(45)
forward(100)


# In[3]:


reset()

forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)


# In[5]:


reset()

forward(50)
right(90)
forward(50)
right(90)
pencolor("red")
forward(50)
right(90)
forward(50)
right(90)


# In[9]:


reset()

size=60

forward(size)
right(90)
forward(size)
right(90)
forward(size)
right(90)
forward(size)
right(90)


# In[10]:


reset()

size=60

print("here")

for i in range(4):
    print("i is ",i)
    forward(size)
    right(90)

print("there")


# In[11]:


reset()

size=60

print("here")

for i in range(4):
    print("i is ",i)
    forward(size)
right(90)

print("there")


# In[12]:


reset()

size=60

print("here")

for i in range(4):
    print("i is ",i)
forward(size)
    right(90)

print("there")


# In[13]:


reset()

size=60

print("here")

for i in range(4):
    print("i is ",i)
forward(size)
right(90)

print("there")


# In[14]:


reset()

size=60

for i in range(4):
    forward(size)
    right(90)



# In[15]:


def square(size):
    for i in range(4):
        forward(size)
        right(90)


# In[18]:


reset()
square(40)

pencolor("red")
square(80)


# In[21]:


reset()
square(40)

penup()
forward(100)
pendown()

square(40)


# In[22]:


def penup_forward(distance):
    penup()
    forward(distance)
    pendown()


# In[23]:


reset()
square(40)

penup_forward(100)

square(40)


# In[ ]:




