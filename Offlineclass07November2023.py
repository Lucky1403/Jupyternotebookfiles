#!/usr/bin/env python
# coding: utf-8

# In[3]:


name = input("Enter your name:-")
print(name)


# In[2]:


#sum of teo numbers using input function
a = int(input("Enter the first number:-"))
b = int(input("Enter the second number:-"))
sum = a+b
print(sum)


# In[6]:


#Sum of two  numbers using map and input function.
x,y,z = map(int,input("enter numbers:").split())
print(x+y+z)


# In[13]:


#Calculating the Profit
A, B, Z = map(int,input("Enter cost  Interior Decoration  Selling Price:").split())
profit = ((Z - (A+B))/(A+B)) *100
print("The profit is:", round(profit,2))


# In[14]:


#print using string Formatting
print("I love {0} and Web {1}".format('coding','Development'))


# In[15]:


#print using String formatting
print("I {1} to {0} Data {2} & {3}".format('learn','want','Structure','Algorithm'))


# In[18]:


#print using string formatting
print("Hello {name} now we are learning {Skill}".format(Skill="Python",name="Alex"))


# In[19]:


#String split
txt = "I love Programming"
x = txt.split(" ")
print(x)


# In[3]:


#In this code we are swapping the value of two variables.
a = 5
b = 7
(a,b)= (b,a)
print(a,b)


# In[5]:


#In this code we are swapping the value of three variables using temp.
a = 10
b = 7
c = 9

temp = a
a = b
b = c
c = temp

print(a,b,c)



# In[6]:


#In this set of practice we are swapping the value of two variables using addition and Subtaction Operators.
a = 100
b = 200

a = a+b
b = a-b
a = a-b
print(a,b)


# In[7]:


#Finding the area of Rectangle
length = float(input("Enter the length of the Rectangle:-"))
breadth = float(input("Enter the breadth of the Rectangle:-"))
area = length*breadth

print("The area of the Rectangle is:",area)


# In[8]:


#finding the area of the square
side = float(input("Enter the length of the side:-"))
area = side**2

print("The area of the square is:-",area)


# In[15]:


print("C++ \nC \nPython")


# In[16]:


print("Java \Kotlin \Swift")


# In[17]:


print("HTML \tCSS")


# In[27]:


pi = 3.14159265359
print('The value of pi is %.2f'%pi)


# In[28]:


pi = 3.14159265359
print('The value of pi is %.4f'%pi)


# In[29]:


pi = 3.14159265359
print('The value of pi is %.5f'%pi)


# In[ ]:




