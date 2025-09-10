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


# In[ ]:


from random import randint,choice


# In[19]:


reset()

penup()
x,y=randint(-100,100), randint(-100,100)
goto(x,y)
pendown()

# if x>0 and y>0:
#     pencolor("red")

# random color
pencolor(choice(["red","green","blue","black","orange","purple"]))
square(20)

penup()
x,y=randint(-100,100), randint(-100,100)
goto(x,y)
pendown()

pencolor(choice(["red","green","blue","black","orange","purple"]))
square(20)


# In[37]:


randint(200,300)


# In[28]:


bob=3

if bob>10:
    print("big")
    print("huge")
elif bob>6:
    print("medium")
else:
    print("small")
    print("tiny")

print("done")


# In[29]:


if shape=="square":
    do_something()
elif shape=="triangle":
    do_something_else()
elif shape=="pentagon":
    do_another_thing()
else:
    print("Invalid shape")


# In[30]:


def twice_with_return(x):
    return x*2

def twice_with_print(x):
    print(x*2)


# In[31]:


twice_with_print(5)


# In[32]:


twice_with_return(5)


# In[33]:


twice_with_return(5)*10


# In[34]:


twice_with_print(5)*10


# In[ ]:




