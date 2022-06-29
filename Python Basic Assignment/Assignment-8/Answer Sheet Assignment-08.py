#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Is the Python Standard Library included with PyInputPlus');get_ipython().run_line_magic('pinfo', 'PyInputPlus')

--> PyInputPlus is not a part of the Python Standard Library, so you must install it separately using Pip

get_ipython().system('pip install pyinputplus')


# In[ ]:


get_ipython().set_next_input('2. Why is PyInputPlus commonly imported with import pyinputplus as pypi');get_ipython().run_line_magic('pinfo', 'pypi')


-->  pypi is alias of PyInputPlus. 


# In[ ]:


3. How do you distinguish between inputInt() and inputFloat()?

--> inputInt() : Accepts an integer value, and returns int value
    inputFloat() : Accepts integer/floating point value and returns float value


# In[ ]:


4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?


--> In the inputint() function we can set the min = 0 and max =99 to ensure user enters number between 0 and 99
pyip.inputInt(min = 0, max =99)


# In[ ]:


get_ipython().set_next_input('5. What is transferred to the keyword arguments allowRegexes and blockRegexes');get_ipython().run_line_magic('pinfo', 'blockRegexes')

--->We can also use regular expressions to specify whether an input is allowed or not. 
The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input.


# In[ ]:


get_ipython().set_next_input('6. If a blank input is entered three times, what does inputStr(limit=3) do');get_ipython().run_line_magic('pinfo', 'do')


--> RetryLimitException (below shown)


# In[1]:


get_ipython().system('pip install pyinputplus')


# In[3]:


import pyinputplus as pyip


# In[11]:


data  = pyip.inputStr(limit=4)
data


# In[ ]:


get_ipython().set_next_input("7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do");get_ipython().run_line_magic('pinfo', 'do')

--> the function returns the default value 


# In[10]:


data1 = pyip.inputStr(limit=3, default='hello')
data1


# In[ ]:





# In[ ]:




