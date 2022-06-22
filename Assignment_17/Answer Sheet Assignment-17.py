#!/usr/bin/env python
# coding: utf-8

# 1. Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal to 7.

# In[1]:


def test():
    guess_me = 7
    entry = int(input("Enter the value: "))
    if entry < guess_me:
        print("Entered value is too low")
    elif entry > guess_me:
        print("Entered value is too high")
    else:
        print("Entered value is just right")
        
   


# In[2]:


test()


# In[3]:


test()


# In[4]:


test()


# 2. Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while loop that compares start with guess_me. Print too low if start is less than guess me. If start equals guess_me, print 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and exit the loop. Increment start at the end of the loop.

# In[23]:


guess_me = 7
start = 1
end = 10
while start< end:
    if start < guess_me :
        print("To low")
    elif start == guess_me:
        print("found it")
        break
    start += 1
while start< end:
    if start < guess_me :
        print("To low")
    else:
        print("oops")
        break
    start += 1


# 3. Print the following values of the list [3, 2, 1, 0] using a for loop.

# In[27]:


list = [3, 2, 1, 0] 

for i in list:
    print(i, end =" ")


# 4. Use a list comprehension to make a list of the even numbers in range(10)

# In[35]:


lst = []
for i in range(1,10):
    if i%2 == 0:
        lst.append(i)
print(lst)


# 5. Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the keys, and use the square of each key as its value.

# In[37]:


dic = {}
for i in range(10):
    dic[i] = i*i
print(dic)


# 6. Construct the set odd from the odd numbers in the range using a set comprehension (10).

# In[53]:


odd = set()
for i in range(10):
    if i%2 != 0 :
        odd.add(i)
print(odd)
        
        
        


# 7. Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10). Iterate through this by using a for loop.

# In[58]:


for i in range(10):
    print("Got_" + str(i), end = " ")


# 8. Define a function called good that returns the list ['Harry', 'Ron', 'Hermione'].

# In[69]:


def good():
    lst = ['Harry', 'Ron', 'Hermione']
    return lst
print(good())


# 9. Define a generator function called get_odds that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.

# In[64]:


def get_odds():
    lst_1 = []
    
    for i in range(10):
        if i%2 != 0: 
            lst_1.append(i)
    yield lst_1

next(get_odds())[2]


# 10. Define an exception called OopsException. Raise this exception to see what happens. Then write the code to catch this exception and print 'Caught an oops'.

# In[99]:


class OopsException(Exception):
    pass

def test(input):
    try:
        if input<0:
            raise OopsException("Caught an oops ")
            
    except OopsException as e:
        print(e)


# In[102]:


test(-4)


# 11. Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a monster', 'A haunted yarn shop'].

# In[108]:


titles = ['Creature of Habit', 'Crewel Fate'] 
plots = ['A nun turns into a monster', 'A haunted yarn shop']

x = zip(titles, plots)

print(dict(x))


# In[ ]:




