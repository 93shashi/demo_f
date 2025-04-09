#1. IP validation 

import re
reg = r"^((25[0-5]|2[0-4][0-9]|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4][0-9]|1\d\d|[1-9]?\d)$"

def checkip(Ip):
    if (re.search(reg, Ip)):
        print("valid Ip")

    else:
        print("Invalid Ip")
Ip = "192.168.0.1"
checkip(Ip)

#2. Python script reverses only the alphabetic characters in the string while keeping the special characters in their original positions
str1= "a!bcd#$e%^f"
strlist = list(str1)
i = 0
j = len(strlist)-1
while i < j:
    if not strlist[i].isalpha():
        i += 1
    elif not strlist[j].isalpha():
        j -= 1
    else:
        strlist[i], strlist[j] = strlist[j], strlist[i]
        i += 1
        j -= 1
str2 = ''.join(strlist)
print("original list is:{0} ,reverse string is:{1}" .format(str1,str2))

#3. simple string reverse: using function
def reverse(str3):
    string4 = ""
    for i in str3:
        string4 = i+string4
    return string4            
str3 = "asdfgh"
print("original string is {0}, reverse string is {1}" .format(str3,reverse(str3)))
#print(reverse(str3))

L1=[2,5,8,5]
L2 = [4,6,7,89]

L1 = print(L1+L2)
T1 = (1,3,4,6,7)
T2 = (2,4.5,6,0)

T1 = print(T1+T2)

class person():
    def __init__(self, name,id):
        self.name = name
        self.id = id

    def display(self):
        print("name of person:", self.name)
        print("id of person:",self.id)
name = 12345
P1 = person(name,"id")
P1.display()
id = 76
name = "ram"
#P1.display(id,name)
'''
a = int(input())
b = int(input())
c = int(input())
d = b-a
print(d)
v = c-b
print(v)'''
#convert string to dict in python

s5 = "hello=123,hiii=234,ram=12"

list5 = []
for i in s5.split(','):
    x = i.split('=')
    list5.append(x)
d = dict(list5)

d1 = {}
for k,v in d.items():
    d1[k] = int(v)
print("dict is d1:",d1)


#setter and getter mothod in python

class person:

    def SetName(self,name):
        self.name = name
    def GetName(self):
        return self.name
P1 = person()
P1.SetName("shashi")
print(P1.GetName())


#fac
def fac(n):
    if (n == 1 & n==0):
        return 1
    else:
        return n*fac(n-1)        
n=5
print(fac(n))

#decorotor:

def decor(func):
    def inner(name):
        if name == "shashi":
            print("this is great")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("hello",name,"GNM")
wish("shashi1")
wish("shashi")

#classmethos

class animal():
    legs = 4
    @classmethod
    def display(cls, name):
        #cls.name=name
        print("{} walks with {} legs :" .format(name,cls.legs))

animal.display("dog")

#python programs to handle two exections:

def exc():
    tot = 0
    for x in list:
        tot+=0
    avr = tot/len(list)
    return tot,avr
try:
    t ,a = exc(['']) 
    print("totat = {}, avg = {}" .format(t ,a))
except TypeError:
    print("please provide the numbers")
except ZeroDivisionError:
    print("plese provide the number stirng")


#python labmda function

a = [lambda x=x: x*11 for x in range(1,11)]
for i in a:
    print(i())

from threading import *
def display():
    for i in range(10):

        print("thread started")
th_obj = Thread(target=display)
th_obj1 = Thread(target=display)
th_obj.start()
th_obj1.start()

for i in range(10):
    print("main thread")

#python lambda function

l = [12,34,56,78,89,2,8]
l1 = list(filter(lambda x:x%2==0,l))
print("even number with lambda {0}:".format(l1))
l2 = list(filter(lambda x:x%2!=0,l))
print("odd number should be {}".format(l2))

#python map with lambda
l3 = [1,3,4,6,7,8]
def double(x):
    return 2*x
l4 = list(map(double,l))
print("map",l4)

l8 = [2,4,5,6,7,8,8,8,7]
l9 = list(map(lambda x:2*x, l8))
print(l9)

'''def decor(func):
    def inner(name):
        if name =="shashi":
            print("good morning bahi")
        else:
            func(name)
        return inner
@decor
def wish(name):
    print("Hello",name,"good night")
wish("shahsi")
wish("ramesh")
'''
#python program for class and sttic method:

import datetime, time
from datetime import date
 
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
 
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
 
 
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
 
print(person1.age)
print(person2.age)
 
# print the result
print(Person.isAdult(12))

#python programe to remove string from ith position
def istring(string1,i):

    a = string1[:i]
    b = string1[i+1:]
    return a+b
string1 = "shashikumar"
print(istring(string1,3))


list1 = [2,4,5,6,7,8]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
print(list1)

#==============================
list2 = [23,45,67,89]
res = []
for ele in list2:
    sum = 0
    for digit in str(ele):
        sum+=int(digit)
    res.append(sum)
print(res)


#===========
list1 = [2,4,5,6,7,8]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
print(list1)

#==============================
list2 = [23,45,67,89]
res = []
for ele in list2:
    sum = 0
    for digit in str(ele):
        sum+=int(digit)
    res.append(sum)
print(res)

#========
import logging

log1 = logging.basicConfig(filename='filenew.txt',level=logging.ERROR)

try:
    print()
except Exception as e:
    logging.exception(e)


#===========


from threading import *;import time
s = Semaphore(4)
def wish(name):
    s.acquire()
    for i in range(10):
        print("good morning",end ='')
        time.sleep(5)
        print(name)
    s.release()
t1 = Thread(target=wish,args=("dhoni",))
t2 = Thread(target=wish,args=("shashi",))
t3 = Thread(target=wish,args=("dhoni2",))
t1.start()
t2.start()
t3.start()
t1.join()

#==============
import logging
logging.basicConfig(filename="new.txt",level=logging.ERROR)
try:
    a = int(input("Entere a number"))
    b = int(input("Enter the number"))
    c = a/b
except Exception as e:
    logging.exception(e)
else:
    print("division value is:", c)

#==========
str1 = input("Enter a string")
sub1 = input("enter a sub-string")
Flag = False
pos = -1
n = len(str1)
while True:
    pos = str1.find(sub1,pos+1,n)
    if pos == -1:
        break
    print("position found at", pos)
    Flag =True
if Flag == False:
    print("position not found")
    

import json
import os
#path=os.path("C:\Users\shashi8x\OneDrive - Intel Corporation\Desktop\EII_project\uwcval")
f = open('sample2.json')
data = json.load(f)
print(data['firstName'])
print(data['lastName'])
f.close()


str1 = "shashi"
str2 =""
l = len(str1)-1
while l>=0:
    str2 = str2+str1[l]
    l-=1
print(str2)

#===========
def reverse1():
    S2 = ""
    for i in S1:
        S2 = i+S2
    return S2
S1 = "shashi"
print(reverse1())

import re
def checkIP(IP):
    reg = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if re.search(reg,IP):
        print("valid IP")
    else:
        print("invalid IP")
IP = "10.12.34.67"
checkIP(IP)


#=====
class p1:
    def do(self):
        print("hello you can fly")
    def to(self):
        print("you can do")
class p2(p1):
    def to(self):
        print(" anything, you want")
obj1 = p1()
obj2 = p2()
obj2.to()
#=================
#calculate power value of a number using static method
class cal:
    @staticmethod
    def power(x,n):
        result = x**n
        print('{} to the power of {} is {}'.format(x,n,result))
#call staticmethod
cal.power(5,5)
#===================
#program to call parent constractor by using super keyword.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class emp(person):
    def __init__(self,name,age,id,address):

        super().__init__(name,age)
        self.id=id
        self.address=address
    def display(self):
        print("name of the person is",self.name)
        print("age of the person is:",self.age)
        print("ID of emp is:",self.id)
        print("address of emp is:",self.address)
C1 = emp("shashi",28,105,"marathahalli")
C1.display()

#============
s = input("enter a string")
d = {}
for i in s:
    if i in d.keys():
        d[i] = d[i]+1
    else:
        d[i] = 1
for k,v in d.items():
    print("key is {} value is {} ".format(k,v))

#===========
#move zero at last
def move(arr2):
    return [nonZero for nonZero in arr2 if nonZero!=0] + \
        [Zero for Zero in arr2 if Zero ==0]

if __name__  == '__main__':
    arr2  = [1,7,0,0,12,0,11,14,0,8]
    print(move(arr2))
    
#reverse of list
list1 = [1,3,5,6,7,8,0]
list2= []
for i in list1:
    list2.insert(0,i)
print("Reverse of list1 is:",list2)

#first 20 prime number
def isPrime(n):
    if(n==1 or n==0):
        return False
    for i in range(2 ,n):
        if(n%i==0):
            return False
    return True
N = 20
for i in range(1, N+1):
    if(isPrime(i)):
        print(i,end= " ")

#=============
def isPrime(n):
  
    # Corner case
    if n <= 1:
        return False
  
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False;
  
    return True
  

print("true") if isPrime(11) else print("false") 
 
  
# This code is contributed by Smitha Dinesh Semwal

def isprime(n):
    if(n==0 or n==1):
        return False
    for i in range(2,n):
        if (n%i==0):
            return False
    return True
N =100
for i in range(1,N+1):
    if(isprime(i)):
        print(i, end=" ")

#need to practice more code for product based company

