#!/usr/bin/env python
# coding: utf-8

# # Assignment-6 Day-6

# 1) list1=[1,2,3,4,5,7,8]
# list2=['a','b','c','d','e'] convert into a dictionary in one line code using list comprehension ("without using zip method")

# In[1]:


list1=[1,2,3,4,5,7,8]
list2=['a','b','c','d','e']
c={list1[i]:list2[i] for i in range(len(list2))}
print("dictionary:" + str(c))


# In[ ]:




