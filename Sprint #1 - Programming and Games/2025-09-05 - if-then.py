#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mplturtle import *


# In[2]:


reset()

for i in range(4):
    forward(101)
    right(90)


# In[3]:


def square(size):
    for i in range(4):
        forward(size)
        right(90)   

def forward_penup(length):
    penup()
    forward(length)
    pendown()


# In[5]:


reset()

for i in range(10):
    square(100)
    forward_penup(150)


# In[7]:


reset()

for bob in range(10):
    print(bob)
    square(100)
    forward_penup(150)


# In[8]:


reset()

for bob in range(10):

    if bob<4:
        pencolor("green")
    else:
        pencolor("red")

    square(100)
    forward_penup(150)


# In[10]:


15%6  # modulus == remainder


# In[11]:


15%2  # odd number


# In[12]:


14%2 # even number


# In[14]:


def isodd(number):
    return number%2==1

def iseven(number):
    return number%2==0    


# In[13]:


reset()

for bob in range(10):

    if bob%2==1: # odd
        pencolor("green")
    else:
        pencolor("red")

    square(100)
    forward_penup(150)


# In[15]:


reset()

for bob in range(10):

    if isodd(bob): # odd
        pencolor("green")
    else:
        pencolor("red")

    square(100)
    forward_penup(150)


# In[19]:


reset()

current_color="green"

for bob in range(10):

    if current_color=="green":
        current_color="red"
    else:
        current_color="green"

    pencolor(current_color)
    square(100)
    forward_penup(150)


# In[ ]:




