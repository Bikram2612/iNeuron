#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. What exactly is []?

--> this is the denotation of a list.


# In[ ]:


2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? 
(Assume [2, 4, 6, 8, 10] are in spam.)


# In[1]:


spam = [2,4,6,8,10,]
spam.insert(2, "Hello")
print(spam)


# In[ ]:


Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.


# In[ ]:


3. What is the value of spam[int(int('3' * 2) / 11)]?


# In[4]:


spam = ['a','b','c','d']
c = spam[int(int('3' * 2) / 11)]
print(c)


# In[ ]:


4. What is the value of spam[-1]


# In[51]:


spam = ['a','b','c','d']


# In[5]:


spam[-1]


# In[ ]:


5. What is the value of spam[:2]


# In[ ]:


spam = ['a','b','c','d']


# In[9]:


spam[:2]


# In[ ]:


Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.

6. What is the value of bacon.index('cat')


# In[1]:


bacon = [3.14, 'cat', 11, 'cat', True]

bacon.index('cat')


# In[ ]:


7. How does bacon.append(99) change the look of the list value in bacon


# In[2]:


r = bacon.append(99)
print(bacon) 


# In[ ]:


get_ipython().set_next_input("8. How does bacon.remove('cat') change the look of the list in bacon");get_ipython().run_line_magic('pinfo', 'bacon')


# In[3]:


bacon.remove('cat')
print(bacon)


# In[ ]:


9. What are the list concatenation and list replication operators
--> The operator for list concentration is +, while the operator for replication is *


# In[ ]:


10. What is difference between the list methods append() and insert()?
--> append() will add values to the end of a list while insert() can add them anywhere in the list by specifying index.


# In[ ]:


11. What are the two methods for removing items from a list
--> by using remove() and del statement.


# In[ ]:


12. Describe how list values and string values are identical.
--> list values are similar to string values because both can be passes to len()


# In[ ]:


13. What's the difference between tuples and lists
--> single braces () is used in tuples while in list square braces [] used. 
--> tuples is a immutable collection while list mutable.


# In[ ]:


14. How do you type a tuple value that only contains the integer 42
--> (42)


# In[ ]:


15. How do you get a list value's tuple form? How do you get a tuple value's list form
--> lets say i have a list l1 = [1,2,3].so to get tuples i have to pass through like tuple(l1)


# In[4]:


l1 = [1,2,3]
d = tuple(l1)


# In[5]:


d


# In[ ]:


--> lets say i have a tuple d = (1,2,3).so to get list i have to pass through like list(d)


# In[6]:


t = list(d)


# In[7]:


t


# In[ ]:


16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain
--> They contain references to list values.


# In[ ]:


17. How do you distinguish between copy.copy() and copy.deepcopy()

--> The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will 
do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




