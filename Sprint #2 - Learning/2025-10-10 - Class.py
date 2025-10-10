#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[5]:


state=Board(7,7)
state.board=[random.choice([0,1,2,3,4,5]) for _ in range(49)]
locations=Board(7,7)
locations.board=list(range(49))
locations


# In[6]:


state


# In[10]:


for diag,diag_locations in zip(state.diags(7),locations.diags(7)):
    print(diag,"   ",diag_locations)


# In[ ]:




