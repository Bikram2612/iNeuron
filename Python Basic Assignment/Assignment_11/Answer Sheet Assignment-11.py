#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Create an assert statement that throws an AssertionError if the variable spam is a negative integer.


# In[13]:


spam = int(input(" Enter the Value: "))
assert(spam >= 0)


# In[ ]:


2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon
contain strings that are the same as each other, even if their cases are different 
(that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).


# In[33]:


eggs = "hello"
bacon = "hello"

assert(eggs != bacon)


# In[35]:


eggs = "goodbye"
bacon = "GOODbye"

assert(eggs.lower() != bacon.lower())


# In[ ]:


3. Create an assert statement that throws an AssertionError every time.


# In[38]:


assert (True != True)


# In[39]:


4. What are the two lines that must be present in your software in order to call logging.debug()?

1) import logging 
2) logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# In[ ]:


5. What are the two lines that your program must have in order to have logging.debug() 
get_ipython().set_next_input('send a logging message to a file named programLog.txt');get_ipython().run_line_magic('pinfo', 'programLog.txt')


# In[ ]:


1) import logging
2) logging.basicConfig(filename = "programLog.txt", level=logging.debug, format = '%(asctime)s - %(levelname)s - %(message)s')


# In[ ]:


get_ipython().set_next_input('6. What are the five levels of logging');get_ipython().run_line_magic('pinfo', 'logging')


# In[ ]:


CRITICAL
ERROR
WARNING
INFO 
DEBUG


# In[ ]:


get_ipython().set_next_input('7. What line of code would you add to your software to disable all logging messages');get_ipython().run_line_magic('pinfo', 'messages')


# In[ ]:


--> logging.disable(logging.CRITICAL)


# In[ ]:


get_ipython().set_next_input('8.Why is using logging messages better than using print() to display the same message');get_ipython().run_line_magic('pinfo', 'message')


# In[ ]:


1) to get consistent log messages.
2) Can write to files easily.
3) more easily we can go for search and filter on these log files.
4) Loads of extra metadata just from configuring the log message format once
5) categorize logs based on severity
6) getting logs once code is deployed for better monitoring


# In[ ]:


get_ipython().set_next_input('9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger');get_ipython().run_line_magic('pinfo', 'debugger')


# In[ ]:


The Step In button will move the debugger into a function call. 
The Step Over button will quickly execute the function call without stepping into it. 
The step Out button will quickly execute the rest of the code until it steps out of the function it currently is in.


# In[ ]:


10.After you click Continue, when will the debugger stop ?

--> the debugger will stop when it has reached the 
 1) end of the program or
 2) a line with a breakpoint.


# In[ ]:


get_ipython().set_next_input('11. What is the concept of a breakpoint');get_ipython().run_line_magic('pinfo', 'breakpoint')


# In[40]:


--> breakpoint is a setting on a line of code due to that the debugger to pause 
    when the program execution reaches the line


# In[ ]:





# In[ ]:




