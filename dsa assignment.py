#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
# solution:
arr=[1,5,9,1,12,7,6,6,9]
sum= 8
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==sum:
            print("Pair of integers whose sum is equal to given number are",(arr[i],arr[j]))


# In[10]:


# Q2. Write a program to reverse an array in place? In place means you cannot create a new array.
# You have to update the original array.
# solution:
def reverse(arr):
    start=0
    end= len(arr)-1
    for m in range(0,len(arr)//2):
        array[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1
    return array

array=[10,20,30,40,50,60,70]
reverse(arr)


# In[ ]:


# Q3. Write a program to check if two strings are a rotation of each other?
# solution:
def check(a1,a2):
    if len(a1) != len(a2):
        return False
    match= a1+a1
    if a2 in match:
        return True
    return False

string1="Sonal"
string2="lɐuoS"
if check((string1),(string2)):
    print("Given Strings are rotational of each other")
else:
    print("Given Strings are not rotational of each other")


# In[14]:


# Q4. Write a program to print the first non-repeated character from a string?
# solution:
Str = "sonall"
while Str != "":
    string_len0 = len(Str)
    ch = Str[0]
    Str = Str.replace(ch, "")
    string_len1 = len(Str)
    if string_len1 == string_len0-1:
        print ("First non-repeating character = ",ch)
        break
else:
    print ("No Unique Character Found!")


# In[15]:


# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
# solution:
def TowerOfhanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfhanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfhanoi(n-1, auxiliary, destination, source)
n = 3
TowerOfhanoi(n,'A','B','C')


# In[16]:


# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
# solution:
def isOperator(x):
    if x == "+":
        return True
    if x == "-":
        return True
    if x == "/":
        return True
    if x == "*":
        return True
    return False
def postToPre(post_exp):
    s = []
    length = len(post_exp)
    for i in range(length):
        if (isOperator(post_exp[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1
            s.append(temp)
        else:
            s.append(post_exp[i])
 
    ans = ""
    for i in s:
        ans += i
    return ans
if __name__ == "__main__":
 
    post_exp = "AB+CD-"
    print("Prefix : ", postToPre(post_exp))


# In[17]:


# Q7. Write a program to convert prefix expression to infix expression.
# solution:
def prefixToInfix(prefix):
    stack = []
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
    return stack.pop()
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
    
str = "*-A/BC-/AKL"
print("infix is:",prefixToInfix(str))


# In[ ]:


# Q8. Write a program to check if all the brackets are closed in a given code snippet.
# solution:
def check_brackets(s):
    stack=[]
    for i in range(len(str)):
        if (str[i]=="[" or str[i]=="{" or str[i]=="("):
            stack.append(str[i])
        elif (len(stack)!=0 and stack[-1]=="[" and str[i]=="]"):
            stack.pop()
        elif (len(stack)!=0 and stack[-1]=="{" and str[i]=="}"):
            stack.pop()
        elif (len(stack)!=0 and stack[-1]=="(" and str[i]==")"):
            stack.pop()
        else:
            return False
    if len(stack)==0:
        return True
    else:
        return False
str="[{()}]"
check_brackets(str)


# In[18]:


# Q9. Write a program to reverse a stack.
# solution:
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def display(self):
        for data in reversed(self.items):
            print(data)
def insert_at_bottom(s, data):
    if s.is_empty():
        s.push(data)
    else:
        popped = s.pop()
        insert_at_bottom(s, data)
        s.push(popped)
def reverse(s):
    if not s.is_empty():
        popped = s.pop()
        reverse(s)
        insert_at_bottom(s, popped)
 
 
        
s = Stack()
data_list = input('Please enter the elements to push: ').split()
for data in data_list:
    s.push(int(data))
 
print('The stack:')
s.display()
reverse(s)
print('After reversing:')
s.display()


# In[20]:


# Q10. Write a program to find the smallest number using a stack.
# solution:     
arr = [3, 12, 44, 79, 22]
x = arr[0]      
for i in range(0, len(arr)):  
    if(arr[i] < x):    
        x = arr[i];    
     
print("Smallest element present in given array is",x)


# In[ ]:




