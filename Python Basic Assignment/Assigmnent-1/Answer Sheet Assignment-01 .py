#!/usr/bin/env python
# coding: utf-8

# In[4]:


Q1. In the below elements which of them are values or an expression? 
eg:- values can be integer or string and expressions will be mathematical operators.
    
* 
'hello'
-87.8
- 
()
+
6 

Ans-1:

* is an expression.
'hello' is a value.
-87.8 is a value.
- is a an expression.
is(a, an, expression.)
+ is a an expression.
6 is a value.


# In[6]:


get_ipython().set_next_input('Q2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')

Ans-2: String is a sequence of characters, which user can represents single('') or double("") quotes.
       Variables refers other values which can be changed.
    


# In[ ]:


3. Describe three different data types.

Ans-3 :
    1) Integer - It stores numerical values. eg:- 1,2,3
    2) String - It stores sequence of characterswhich user can represents single('') or double("") quotes.
       eg:- "Bikram", "Nath", 'iNeuron'
    3) Bool - It hold a boolean value, true or false.


# In[29]:


get_ipython().set_next_input('4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')

Ans-4 :
    An expression made up of mathematical operators. Expression do mathematical operations like +, -,*, /.


# In[30]:


get_ipython().set_next_input('5. This assignment statements, like spam = 10. What is the difference between an expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')

Ans-5 :
    Expression is made up of values, containers, and mathematical operators
    Statement is just like a command.
    


# In[16]:


# 6. After running the following code, what does the variable bacon contain?

bacon = 22
bacon + 1

#Ans-6: 23


# In[17]:


"7. What should the values of the following two terms be?"

'spam' + 'spamspam'
Ans:- 'spamspamspam'
    
'spam' * 3
Ans:- 'spamspamspam'


# In[27]:


'spam' + 'spamspam'


# In[28]:


'spam' * 3


# In[18]:


get_ipython().set_next_input('8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')

Ans-8:
    Because varible name must be a string as 100 is an integer so it will not consider a a valid variable name.


# In[23]:


get_ipython().set_next_input('9. What three functions can be used to get the integer, floating-point number, or string version of a value');get_ipython().run_line_magic('pinfo', 'value')

Ans-9:
    To get an interger we can use int() function.
    To get a floating-point number we can use float() function.
    To get a string we can use str() function.


# In[25]:


get_ipython().set_next_input('10. Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')
'I have eaten ' + 99 + ' burritos.'

Ans-10 :
    As we know same type of datatypes can be concatinate, but in the above expression 99 is an interger and rest are in
    string format so its showing error. To resolve this error change the datatypes of 99 to string by 
    putting 99 inside '' or "".
    
'I have eaten ' + "99" + ' burritos.'


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




