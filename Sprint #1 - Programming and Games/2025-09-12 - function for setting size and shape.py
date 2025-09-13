#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mplturtle import *


# In[2]:


def draw_shape_with_sides(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        forward(length)
        right(angle)


# In[4]:


reset()
draw_shape_with_sides(5, 100)  # Draw a pentagon with side length 100


# In[5]:


def draw_shape(name,length):
    if name=="triangle":
        draw_shape_with_sides(3,length)
    elif name=="square":
        draw_shape_with_sides(4,length)
    elif name=="pentagon":
        draw_shape_with_sides(5,length)
    elif name=="hexagon":
        draw_shape_with_sides(6,length)
    elif name=="heptagon":
        draw_shape_with_sides(7,length)
    elif name=="octagon":
        draw_shape_with_sides(8,length)
    else:
        print("Shape not recognized")


# In[8]:


reset()
draw_shape("hexagon", 80)  # Draw a hexagon with side length 80
draw_shape("triangle", 60)  # Draw a triangle with side length 60


# In[ ]:




