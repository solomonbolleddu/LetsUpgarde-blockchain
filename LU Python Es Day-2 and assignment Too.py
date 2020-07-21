#!/usr/bin/env python
# coding: utf-8

# # Back Slash

# In[1]:


print("Barcelone is 
      the best")


# I correct it by using \.

# In[3]:


print("Barcelone is the best")


# # Triple Quotes

# In[8]:


print("""(”)….(”)
( ‘ o ‘ )
(”)–(”)
(””’)-(””’)""")


# Next example that it produces a doc string.

# In[10]:


"""(”)….(”)
( ‘ o ‘ )
(”)–(”)
(””’)-(””’)"""


# # String inside the quotes.

# consider,

# In[11]:


print("bienvenue")


# it if works with single quotes.

# In[12]:


print('bienvenue')


# but if in a statement if apostrophe comes 

# In[13]:


print('my phone's charger)


# it won't work we can use two methods to correct this--
# first use double quotes:

# In[14]:


print("my phone's charger")


# or else use backslash:

# In[15]:


print('my phone\'s charger')


# # Escape sequence of string

# if you want to make space between the two string then use \t.

# In[16]:


print("blah\tblah\tblah")


# if you want it in the next line then use \n.

# In[17]:


print("blah\nblah\nblah")


# # Formatted output

# In[20]:


x="itachi"
y=97.444
z=23
print("the name is",x,"marks are",y,"and age is",z)


# this is first example and next one.

# In[22]:


print("the name is %s marks are %f and the age is %d"%(x,y,z))


# if u need spaces in the values then use %10.

# In[23]:


print("the name is %10s marks are %10f and the age is %10d"%(x,y,z))


# to get accuracy in the marks use .2 or .3 or any places.

# In[24]:


print("the name is %s marks are %.2f and the age is %d"%(x,y,z))


# by using f string you can compile also.

# In[25]:


print(f"the name is {x} marks are {y} and the age is {z}")


# # Python variables

# you can use anything as variable but not predefined keywords. forexample 

# In[27]:


if =10


# but it will accept this see

# In[28]:


if1=10


# it can't use number in the starting of the variable. 

# In[29]:


10a=1


# but it can take like this 

# In[30]:


a10=1


# it also takes underscore as a variable.

# In[31]:


_=2


# # Python assignment statement

# In[32]:


a=b=10


# In[33]:


a


# In[34]:


b


# In[35]:


j=20


# In[36]:


id(j)


# if k is also assigned 20 then j and k will have same address location. 

# In[38]:


k=20


# In[39]:


id(k)


# you can delete the binding by use del

# In[40]:


del k


# In[41]:


k


# but it wont delete the address location as still j holds the value 

# In[42]:


j


# # Arithmetic operators

# Addtion,Substraction,Multiplication,Division respectively 

# In[43]:


5+2


# In[44]:


5-2


# In[45]:


5*2


# In[46]:


5/2


# for exponention(pow), modulus and floor division

# In[47]:


5**2


# In[48]:


5%2


# In[49]:


5//2


# # Comparison operators

# if both the values are equal it sends true

# In[55]:


a=10
b=20
a==b


# In[56]:


c=10
a==c


# greater, lesser, greaterthan, lesserthan respectively

# In[57]:


a>c


# In[58]:


a<c


# In[59]:


a>=c


# In[60]:


a<=c


# not equal to operator

# In[62]:


a!=b


# In[63]:


a!=c


# # Bitwise operators

# operators like |, & and ^

# In[68]:


a=240
b=1
a|b


# In[69]:


a&b


# In[70]:


a^b


# and to get binary values

# In[73]:


bin(a)


# In[74]:


bin(b)


# # Logical operators

# In[75]:


a=1
b=20
a>20


# according to the truth tables we take some examples

# In[76]:


a>20 or 10>9


# the above is for or and the below is for or

# In[77]:


a>20 and 10>9


# in some cases it happens this coz m is not assigned in the begin

# In[78]:


10>9 & 20>m


# but again if the first condition is false it  doesn't even check it delivers false 

# In[79]:


10<9 & 20>m


# not operator

# In[80]:


10<9


# In[81]:


not 10<9


# # Membership operators

# using of in and not in operators

# In[83]:


str1 ="lifeisgood"
"a" in str1


# In[84]:


"a" not in str1


# # Identity operator

# using of is or is not operators

# In[85]:


a=90
b=90
a==b


# In[86]:


a is b


# it returns true cause the address location is same 

# In[87]:


a is not b


# the range between -5 to 256 all the integers will return true else false

# In[89]:


a=256
b=256
a is b


# In[90]:


a=-6
b=-6
a is b


# even float value returns false

# In[91]:


a=1.5
b=1.5
a==b


# In[92]:


a is b


# # Operator precedence

# In[93]:


10+10/2-4


# In[ ]:




