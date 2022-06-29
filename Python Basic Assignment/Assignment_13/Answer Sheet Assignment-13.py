#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. What advantages do Excel spreadsheets have over CSV spreadsheets');get_ipython().run_line_magic('pinfo', 'spreadsheets')
--> In Excel, spreadsheets can have values of data types other than strings; 
   cells can have different fonts, sizes, or color settings; 
   cells can have varying widths and heights; adjacent cells can be merged; and you can embed images and charts.


# In[ ]:


get_ipython().set_next_input('2. What do you pass to csv.reader() and csv.writer() to create reader and writer objects');get_ipython().run_line_magic('pinfo', 'objects')

---> just pass a File object, by call to open().


# In[ ]:


get_ipython().set_next_input('3. What modes do File objects for reader and writer objects need to be opened in');get_ipython().run_line_magic('pinfo', 'in')
--> file objects need to be opened in read-binary ('rb') for Reader objects 
    and write-binary ('wb') for Writer objects.


# In[ ]:


get_ipython().set_next_input('4. What method takes a list argument and writes it to a CSV file');get_ipython().run_line_magic('pinfo', 'file')
--> writerow() method


# In[ ]:


get_ipython().set_next_input('5. What do the keyword arguments delimiter and line terminator do');get_ipython().run_line_magic('pinfo', 'do')

--> The delimiter argument changes the string used to separate cells in a row. 
    The lineterminator argument changes the string used to separate rows.


# In[ ]:


get_ipython().set_next_input('6. What function takes a string of JSON data and returns a Python data structure');get_ipython().run_line_magic('pinfo', 'structure')

--> json.loads()


# In[ ]:


get_ipython().set_next_input('7. What function takes a Python data structure and returns a string of JSON data');get_ipython().run_line_magic('pinfo', 'data')

--> json.dumps()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




