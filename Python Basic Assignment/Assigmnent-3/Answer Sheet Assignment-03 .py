#!/usr/bin/env python
# coding: utf-8

# In[6]:


1. Why are functions advantageous to have in your programs.

Ans: code reusabilit,improve maintainability and scalability.


# In[ ]:


2.When does the code in a function run: when it's specified or when it's called

Ans: when it called at that time the code inside a function run.


# In[9]:


3.What statement creates a function.

Ans: function is created by def keyword followed by function name, round brackets and a colon.
    


# In[ ]:


get_ipython().set_next_input('4. What is the difference between a function and a function call');get_ipython().run_line_magic('pinfo', 'call')

A function is a block of code that does a particular operation and returns a result.
A function call is the code used to pass control to a function.


# In[ ]:


get_ipython().set_next_input('5. How many global scopes are there in a Python program? How many local scopes');get_ipython().run_line_magic('pinfo', 'scopes')

--> one global scope is there.


# In[ ]:


6. What happens to variables in a local scope when the function call returns

--> The local variable can be used outside the function any time after the function call completes.


# In[ ]:


get_ipython().set_next_input('7.What is the concept of a return value? Is it possible to have a return value in an expression');get_ipython().run_line_magic('pinfo', 'expression')

--> the values that a function returns when it has completed. yes it is possible to have.


# In[ ]:


get_ipython().set_next_input('8. If a function does not have a return statement, what is the return value of a call to that function');get_ipython().run_line_magic('pinfo', 'function')
--> it returns None


# In[ ]:


9. How do you make a function variable refer to the global variable
--> by using global keyword.


# In[ ]:


get_ipython().set_next_input('10. What is the data type of None');get_ipython().run_line_magic('pinfo', 'None')

--> print is a datatype of none


# In[ ]:


get_ipython().set_next_input('11. What does the sentence import areallyourpetsnamederic do');get_ipython().run_line_magic('pinfo', 'do')
--> imports a module named areallyourpetsnamederic.


# In[ ]:


get_ipython().set_next_input('12. If you had a bacon() feature in a spam module, what would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')
--> spam.bacon()


# In[ ]:


get_ipython().set_next_input('13. What can you do to save a programme from crashing if it encounters an error');get_ipython().run_line_magic('pinfo', 'error')

--> by handling the exception using try and except.


# In[ ]:


get_ipython().set_next_input('14. What is the purpose of the try clause? What is the purpose of the except clause');get_ipython().run_line_magic('pinfo', 'clause')

-->  The code inside the try block will execute when there is no error in the program.
Whereas the code inside the except block will execute whenever the program encounters 
some error in the preceding try block.

