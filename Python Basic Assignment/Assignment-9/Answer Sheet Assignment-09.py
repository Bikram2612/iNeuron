#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. To what does a relative path refer');get_ipython().run_line_magic('pinfo', 'refer')

--> reffered as current working directory.


# In[ ]:


get_ipython().set_next_input('2. What does an absolute path start with your operating system');get_ipython().run_line_magic('pinfo', 'system')
--> C:\Windows


# In[ ]:


get_ipython().set_next_input('3. What do the functions os.getcwd() and os.chdir() do');get_ipython().run_line_magic('pinfo', 'do')


# In[9]:


os.getcwd() # to get the current work directory


# In[10]:


os.chdir()
--> os.chdir() method in used to change the current working directory to specified path


# In[ ]:


get_ipython().set_next_input('4. What are the . and .. folders');get_ipython().run_line_magic('pinfo', 'folders')

The . folder is the current folder, and .. is the parent folder.


# In[ ]:


get_ipython().set_next_input('5. In C:\\bacon\\eggs\\spam.txt, which part is the dir name, and which part is the base name');get_ipython().run_line_magic('pinfo', 'name')

--> C:\bacon\eggs is the dir name, while spam.txt is the base name.


# In[ ]:


get_ipython().set_next_input('6. What are the three “mode” arguments that can be passed to the open() function');get_ipython().run_line_magic('pinfo', 'function')

--> The string 'r' for read mode, 'w' for write mode, and 'a' for append mode


# In[ ]:


get_ipython().set_next_input('7. What happens if an existing file is opened in write mode');get_ipython().run_line_magic('pinfo', 'mode')

--> if an existing file opened in write mode it will erased.


# In[ ]:


8. How do you tell the difference between read() and readlines()?

--> The read() method returns the file's entire contents as a single string value. 
The readlines() method returns a list of strings, where each string is a line from the file's contents.


# In[ ]:


get_ipython().set_next_input('9. What data structure does a shelf value resemble');get_ipython().run_line_magic('pinfo', 'resemble')

-->A shelf value resembles a dictionary value


# In[ ]:




