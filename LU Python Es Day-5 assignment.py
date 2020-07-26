#!/usr/bin/env python
# coding: utf-8

# # Assignment-5 Day-5

# 1) [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4] sort this in increasing order but all the zeros should be at the right hand side

# In[2]:


a=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
a.sort()
b=a.count(0)
print(a[b:]+a[:b])


# 2)list1=[10,20,40,60,70,80]
#   list2=[5,15,25,35,45,60]
# merge these two sorted lists and produce a single sorted list, but use only single loop and dont use sort()

# In[5]:


list1=[10,20,40,60,70,80] 
list2=[5,15,25,35,45,60]
listA=list1+list2
listB=[]
for a in range(min(listA),max(listA)+1):
    if a in listA:
        listB.append(a)
print(listB)


# In[ ]:




