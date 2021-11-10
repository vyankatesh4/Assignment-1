#!/usr/bin/env python
# coding: utf-8

# In[18]:


series = (1,2,3,4,5,6,7,8,9)
count_odd = 0
count_even = 0
for i in series:
    if i%2 ==1:
        count_odd+=1
    else:
        count_even+=1
print('Number of even numbers:',count_even)
print("Number of odd numbers:",count_odd)


# In[ ]:




