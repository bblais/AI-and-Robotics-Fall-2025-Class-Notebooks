#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pylab import *


# In[2]:


from Game import Storage


# In[4]:


Q=0
t=0

α=0.1

_S=Storage()

_S+=t,Q
for i in range(1000):

    r=rand()
    if r<0.9:
        reward=1
    else:
        reward=0

    Q+=α*(reward-Q)  # push toward the reward
    t+=1

    _S+=t,Q

t,Q=_S.arrays()
plot(t,Q)



# In[5]:


Q=0
t=0

α=0.01

_S=Storage()

_S+=t,Q
for i in range(1000):

    r=rand()
    if r<0.9:
        reward=1
    else:
        reward=0

    Q+=α*(reward-Q)  # push toward the reward
    t+=1

    _S+=t,Q

t,Q=_S.arrays()
plot(t,Q)



# In[ ]:




