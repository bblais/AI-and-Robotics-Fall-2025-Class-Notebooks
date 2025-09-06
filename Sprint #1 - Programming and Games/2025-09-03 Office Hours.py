#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mplturtle import *


# In[3]:


reset()
forward(101)
right(90)
forward(101)
right(90)
forward(101)
right(90)
forward(101)
right(90)


# In[8]:


size=153
reset()
print("here also outside")
for i in range(4):
    forward(size)
    right(90)
    print("inside loop")


print("outside the loop")


# In[10]:


size=153
reset()
print("here also outside")
for bob in range(4):
    forward(size)
    right(90)
    print("inside loop")
    print("bob is", bob)

print("outside the loop")


# In[11]:


def square(size):
    for i in range(4):
        forward(size)
        right(90)


# In[12]:


reset()
square(101)


# In[13]:


reset()

for i in range(4):
    size=(i+1)*50
    square(size)


# In[14]:


reset()
square(101)


# In[ ]:




