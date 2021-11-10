#!/usr/bin/env python
# coding: utf-8

# In[69]:


#Write a Python program to get the Fibonacci series between 0 to 50
def fib(n):
    a = 0
    b = 1
 
    for i in range(1,n):
        c = a + b
        a = b
        b = c
        
        print(c,end=' ')
fib(9)


# In[ ]:




