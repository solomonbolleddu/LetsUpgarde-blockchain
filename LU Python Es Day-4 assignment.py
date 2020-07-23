#!/usr/bin/env python
# coding: utf-8

# # Assignment - 4 Day - 4

# 1) write a program to find all the occurences of the substring in the given string along with the index value

# I have used list comprehension + startswith() to find the occurences ***

# In[2]:


a=input("Enter The String\n")
b=input("Enter The Substring\n")  
c= [i for i in range(len(a)) if a.startswith(b, i)]   
print("The Indices of the Substrings are : " + str(c)) 


# 2)write a program to apply islower() and isupper() with different strings.

# im going to use lowercase, uppercase, lower and uppercases, numerical and special keys for two functions

# ----islower()

# case-1 (lowercases)

# In[5]:


str1="bienvenue"
str1.islower()


# case-2 (uppercases)

# In[8]:


str2="BIENVENUE"
str2.islower()


# case-3 (lower and uppercases)

# In[9]:


str3="biENveNue"
str3.islower()


# case-4 (numerical)

# In[12]:


str4="212345"
str4.islower()


# case-5 (lowercase with special keys and number )

# In[14]:


str5="@#$1234bienvenue$$555@@#"
str5.islower()


# ----isupper()

# case-1 (lowercases)

# In[15]:


str1="bienvenue"
str1.isupper()


# case-2 (uppercases)

# In[18]:


str2="BIENVENUE"
str2.isupper()


# case-3(lower and upper cases)

# In[19]:


str3="BiEnVeNUE"
str3.isupper()


# case-4(numerical)

# In[22]:


str4="12345667"
str4.isupper()


# case-5(uppercases with special keys and numbers)

# In[23]:


str5="@@#$$$13245BIENVENUE62787##@@"
str5.isupper()


# In[ ]:




