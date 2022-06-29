#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. What does RGBA stand for');get_ipython().run_line_magic('pinfo', 'for')


# In[ ]:


--> Red, green , blue alpha


# In[ ]:


get_ipython().set_next_input('2.From the Pillow module, how do you get the RGBA value of any images');get_ipython().run_line_magic('pinfo', 'images')


# In[10]:


from PIL import Image

image_object = Image.open(r'C:\Users\My PC\Downloads\X.jpg')
pixels = image_object.convert('RGBA')
data = pixels.getdata()
lofpixels = []
for pixel in data:
    lofpixels.extend(pixel)
print(lofpixels)


# In[ ]:


get_ipython().set_next_input('3. What is a box tuple, and how does it work');get_ipython().run_line_magic('pinfo', 'work')

A box tuple is a tuple value of four integers: the left-edge x-coordinate, the top-edge y-coordinate,the width,
and the height, respectively.


# In[ ]:


get_ipython().set_next_input('4. Use your image and load in notebook then, How can you find out the width and height of an Image object');get_ipython().run_line_magic('pinfo', 'object')


# In[11]:


from PIL import Image
image_obj = Image.open(r'C:\Users\My PC\Downloads\X.jpg')

image_obj.size


# In[14]:


width, height= image_obj.size


# In[15]:


width


# In[16]:


height


# In[17]:


image_obj.filename


# In[18]:


image_obj.format


# In[19]:


image_obj.format_description


# In[ ]:


get_ipython().set_next_input('5. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it');get_ipython().run_line_magic('pinfo', 'it')


# In[26]:


from PIL import Image
img = Image.open('Pic.jpg')
new_img = img.crop((0,50,50,50))


# In[31]:


get_ipython().set_next_input('6. After making changes to an Image object, how could you save it as an image file');get_ipython().run_line_magic('pinfo', 'file')

from PIL import Image
pic = Image.open('pic.jpg')
pic.save('pic2.jpg')


# In[ ]:


get_ipython().set_next_input('7. What module contains Pillow’s shape-drawing code');get_ipython().run_line_magic('pinfo', 'code')

--> Pillows ImageDraw module contains Shape drawing methods


# In[ ]:


get_ipython().set_next_input('8. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object');get_ipython().run_line_magic('pinfo', 'object')

--> ImageDraw objects have shape-drawing methods such as point(), line(), or rectangle().
They are returned by passing the Image object to the ImageDraw.Draw() function.


# In[ ]:





# In[ ]:





# In[ ]:




