#!/usr/bin/env python
# coding: utf-8

# 1.How many seconds are in an hour? Use the interactive interpreter as a calculator 
# and multiply the number of seconds in a minute (60) by the number of minutes in an hour (also 60).

# In[2]:


print(60*60)


# 2. Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.

# In[3]:


seconds_per_hour = 60*60
print(seconds_per_hour)


# 3. How many seconds do you think there are in a day? Make use of the variables seconds per hour and minutes per hour.

# In[6]:


seconds_per_hour = 60*60
minutes_per_hour = 60

print("Total No of seconds in a day: ", seconds_per_hour*24, "Sec")


# 4. Calculate seconds per day again, but this time save the result in a variable called seconds_per_day

# In[8]:


seconds_per_hour = 60*60

seconds_in_a_day = (seconds_per_hour*24)

print(seconds_in_a_day)


# 5. Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.

# In[11]:


seconds_per_hour = float(60*60)
seconds_in_a_day = float(seconds_per_hour*24)

division = (seconds_in_a_day/seconds_per_hour)

print(division)


# 6. Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did this number agree with the floating-point value from the previous question, aside from the final .0?

# In[19]:


seconds_per_hour = 60*60
seconds_in_a_day = seconds_per_hour*24

division = (seconds_in_a_day//seconds_per_hour)

print(division, '--> yes this values agree with the floating point value from the previous question')


# 7. Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

# In[148]:


prime_list= []
def genPrimes():
    lower_num = 0
    upper_num = 20
    
    for i in range(lower_num, upper_num+1):
        if i>1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    print(prime_list)
    
    #object creation for iter function
    
obj_1 = iter(prime_list)


# In[149]:


genPrimes()


# In[150]:


for numbers in range(8):
    print(next(obj_1))


# In[ ]:




