#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mplturtle import *
from random import random


# In[2]:


random()


# In[8]:


reset()
for i in range(300):
    forward(10)

    x,y=position()
    if x>100:
        pencolor("red")
    elif x>50:
        pencolor("green")
    elif x>0:
        pencolor("black")
    elif x>-50:
        pencolor("blue")
    elif x>-100:
        pencolor("purple")
    else:
        pencolor("maroon")

    right(random()*180-90)


# In[4]:


animate()


# In[ ]:




