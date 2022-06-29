#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input("1. What does an empty dictionary's code look like");get_ipython().run_line_magic('pinfo', 'like')
--> An empty dictionary can be created by just placing to curly braces{}.


# In[ ]:


2. What is the value of a dictionary value with the key 'foo' and the value 42?
--> {'foo':42}


# In[ ]:


get_ipython().set_next_input('3. What is the most significant distinction between a dictionary and a list');get_ipython().run_line_magic('pinfo', 'list')
--> The items stored in a dictionary are unordered, while the items in a list are ordered.


# In[ ]:


4. What happens if you try to access spam['foo'] if spam is {'bar': 100}


# In[1]:


spam = {"bar" : 100}
spam["foo"]


# In[ ]:


--> it will show a KeyError.


# In[ ]:


5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam
and 'cat' in spam.keys()?

---> There is no difference. The in operator checks whether a value exists as a key in the dictionary.


# In[ ]:


6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam 
and 'cat' in spam.values()?

--> 'cat' in spam checks whether there is a 'cat' key in the dictionary, 
while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.


# In[ ]:


get_ipython().set_next_input('7. What is a shortcut for the following code');get_ipython().run_line_magic('pinfo', 'code')

if 'color' not in spam:
spam['color'] = 'black'


# In[ ]:


--> spam.setdefault ('color','black')


# In[ ]:


get_ipython().set_next_input('8. How do you "pretty print" dictionary values using which module and function');get_ipython().run_line_magic('pinfo', 'function')
--> pprint.pprint()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




