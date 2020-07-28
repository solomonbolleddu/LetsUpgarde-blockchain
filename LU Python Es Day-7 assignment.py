#!/usr/bin/env python
# coding: utf-8

# # Assignment-7 Day-7

# 1) use the dictionary,
# port1={21:"FTP",22:"SSH",23:"telnet",80:"http"},
# and make a new dictionary in which keys become values and values become keys,
# as shown: port2={"FTP":21,"SSH":22,"telnet":23,"http":80}

# In[2]:


port1={21:"FTP",22:"SSH",23:"telnet",80:"http"}
port2=dict([(value,key) for key,value in port1.items()])
print(port2)


# 2) take a list of tuple as shown below[(1,2),(3,4),(5,6),(4,5)]
# make a new list which contains the sum of the tuples

# In[3]:


a=[(1,2),(3,4),(5,6),(4,5)]
b=[sum(i)for i in a]
print(b)


# 3) take a list as shown [(1,2,3),[1,2],['a','hit','less']]
# the list contains tuples and lists make elements of the inner of the tuples and list to the outer list

# In[4]:


a=[(1,2,3),[1,2],['a','hit','less']]
b=[]
for i in a:
    if type(i)==type(a):
        b=b+i
    elif type(i)==tuple:
        b.extend(i)
    else:
        b.append(i)
print(b)


# In[ ]:




