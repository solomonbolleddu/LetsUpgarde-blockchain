#!/usr/bin/env python
# coding: utf-8

# # Assignment - 3 Day - 3

# 1) write a program to find sum of n numbers with the help of while loop.

# In[10]:


b=int(input("ENTER THE NTH NUMBER\n"))
a=0
while b>0:
    a=a+b
    b=b-1
print("THE SUM OF THE DIGITS ARE\n",a)


# 2) write a program to take an integer and find whether it is prime or not

# In[23]:


b=int(input("ENTER THE NUMBER\n"))
a=0
for c in range(2,b//2+1):
    if b%c==0:
        a=a+1
if a<=0:
    print("its a prime number")
else:
    print("its a composite number")

