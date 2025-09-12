#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mplturtle import *


# In[2]:


def square(size):
    for _ in range(4):
        forward(size)
        right(90)


# In[4]:


reset()
square(50)


# In[14]:


reset()

current_color="black"

for j in range(5):

    # draw row
    for i in range(5):
        pencolor(current_color)
        square(50)

        if current_color == "black":
            current_color = "red"
        else:
            current_color = "black"

        print(i)
        penup()
        forward(80)
        pendown()

    # move over
    penup()
    right(90)
    forward(80)
    right(90)
    forward(400)
    right(180)
    pendown()




# In[15]:


reset()


count=0

for j in range(5):

    # draw row
    for i in range(5):

        if count % 2 == 0:
            pencolor("black")
        else:
            pencolor("red")

        square(50)
        count=count+1

        if current_color == "black":
            current_color = "red"
        else:
            current_color = "black"

        print(i)
        penup()
        forward(80)
        pendown()

    # move over
    penup()
    right(90)
    forward(80)
    right(90)
    forward(400)
    right(180)
    pendown()




# In[ ]:




