#!/usr/bin/env python
# coding: utf-8

# In[1]:


1. How do you distinguish between shutil.copy() and shutil.copytree()?

--> The shutil.copy() function will copy a single file, 
while shutil.copytree() will copy an entire folder, along with all its contents


# In[ ]:


get_ipython().set_next_input('2. What function is used to rename files');get_ipython().run_line_magic('pinfo2', 'files')

--> shutil.move() function is used for renaming files,


# In[ ]:


get_ipython().set_next_input('3. What is the difference between the delete functions in the send2trash and shutil modules');get_ipython().run_line_magic('pinfo', 'modules')

--> The send2trash functions will move a file or folder to the recycle bin,
while shutil functions will permanently delete files and folders.


# In[ ]:


4.ZipFile objects have a close() method just like File objects’ close() method.
get_ipython().set_next_input('What ZipFile method is equivalent to File objects’ open() method');get_ipython().run_line_magic('pinfo', 'method')

---> ZipFile() function is equivalent to the open() function; the first argument is the filename, 
and the second argument is the mode to open the ZIP file in (read, write, or append).


# In[ ]:


5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf or .jpg).
Copy these files from whatever location they are in to a new folder.


# # To get the files from the given path & copy the files.

# In[5]:


import os
import glob
import shutil
import logging

logging.basicConfig(filename= "File_opr.log", level= logging.DEBUG, format= "%(asctime)s %(levelname)s %(message)s")

class file_opr:
    
    def file_copy(self): 
        """ To filter out the desired file extension form given path & copy the files to desired destination"""   
        try:
            logging.info("The code is executed successfully")
            logging.debug("Debugging successfully done")
           
            path = str(input(" Enter the Path : "))
            if path == "" :
                raise Exception("Invalid Path")
            ext = (".jpg", ".xlsx",".png")
            for file in os.listdir(path):                             
                if file.endswith(ext):
                    print(file)
            
            source_dir = path                                                    
            destination_dir = "C:/Users/My PC/Desktop/b"
            for f in glob.iglob(os.path.join(source_dir, "*.jpg")):
                     shutil.copy(f, destination_dir)
            print("Successfully copied")
                     
        except Exception as e:
                     logging.error("Errog has happend ")
                     logging.exception("Exception occured " + str(e))
                     print(str(e))


# In[6]:


obj  = file_opr()


# In[7]:


obj.file_copy()


# In[8]:


logging.shutdown()


# In[ ]:




