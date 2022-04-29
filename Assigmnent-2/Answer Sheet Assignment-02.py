#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')

Ans-1 : True & False. In Python, boolean variables are defined by the True and False keywords.


# In[ ]:


get_ipython().set_next_input('2.What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')

Ans-2: 
    AND, OR, NOT


# In[ ]:


3. Make a list of each Boolean operator's truth tables 
(i.e. every possible combination of Boolean values for the operator and what it evaluate ).

Ans 3:
    AND OPERATOR
    
    A(INPUT 1)    B(INPUT 2)   OUTPUT
    True             True        True
    False            False       False
    True             False       False
    False            True        False
    
    
OR OPERATOR
    
    A(INPUT 1)    B(INPUT 2)   OUTPUT
    True             True        True
    False            False       False
    True             False       True
    False            True        True
    

NOT OPERATOR
    
    A(INPUT 1)       OUTPUT
    True             False
    False            True
   


# In[7]:


#4. What are the values of the following expressions?

#Ans 4:

(5 > 4) and (3 == 5)


# In[8]:


not (5 > 4)


# In[9]:


(5 > 4) or (3 == 5)


# In[10]:


not ((5 > 4) or (3 == 5))


# In[26]:


(True and True) and (True == False)


# In[12]:


(not False) or (not True)


# In[27]:


#5 What are the six comparison operators?

# Ans: ==, !=, >, >=, <, <=.


# In[28]:


#6 . How do you tell the difference between the equal to and assignment operators?
     #Describe a condition and when you would use one.

Ans:

== is used to check the equality and = is used to assign any variable.

For eg- if there is any variable named a then,

a==3 → it will check whether a is 3 or not

a=3 → it will assign a to 3 .


# In[4]:


# 7. Identify the three blocks in this code.

#Ans:

spam = 0
if spam == 10:
    print('eggs')        # indent increased, block A
    if spam > 5:         # still block A
        print('bacon')   # still block A, indent increased, block B inside block A
    else:                # still block A, indent decreased, block B ended in line above
        print('ham')     # still block A, indent increased, block C inside block A
    print('spam')        # still block A, indent decreased, block C ended in line above
print('spam')  


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam,
and prints Greetings! if anything else is stored in spam.


# In[5]:


spam = int(input("Enter the Value "))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
    


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')

Ans: Ctrl+C


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')

--> The break statement will terminate the loop containing it and controls the program flow to the statement 
after the body of the loop.
--> The continue statement used to skip the code inside loop for the current iteration.


# In[16]:


for i in "Bikram":
    if i=="k":
        break
    print(i)
print("The end")


# In[15]:


for i in "Bikram":
    if i=="k":
        continue
    print(i)
print("The end")


# In[25]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

Ans:- 
a) range(10)

range(stop):
here we are passing only one argument to the range(), which is basically the end or stop range, 
it will generate a sequence of integers starting from 0 to stop -1.
Here, start = 0 and step = 1 as a default value.

return--> 0,1,2,3,4,5,6,7,8,9.


b) range(0,10)

range(start, stop)
here we are passing two argument to the range(), which is basically the start and stop range,
it will generate integers starting from the start number to stop -1.
Here, the step = 1 as a default value.

return--> 0,1,2,3,4,5,6,7,8,9.

c) range(0,10,1)
range(start, stop, step)
here we are passing three argument to the range(), which is basically the start and stop range with step size,
it will generate a sequence of numbers, starting from the start number, increments by step number, 
and stops before a stop number.

return--> 0,1,2,3,4,5,6,7,8,9.


# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop. 
Then write an equivalent program that prints the numbers 1 to 10 using a while loop.


# In[15]:


for i in range(1,11):
    print(i ,end = " ")


# In[14]:


i = 1
while i<11:
    print(i, end = " ")
    #i=i+1
    i += 1


# In[ ]:


get_ipython().set_next_input('13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')

ans:- spam.bacon().

