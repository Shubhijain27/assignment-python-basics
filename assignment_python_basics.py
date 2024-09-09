# -*- coding: utf-8 -*-
"""assignment python basics

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hWH5Yui1h5p-sQyxtEK7hhQlW7WxuOhV
"""



"""# EXPLAIN THE KEY FEATURES OF PYTHON THAT MAKE IT A POPULAR CHOICE FOR PROGRAMMING
 ANSWER :

1. **Free and Open Source**

Python language is freely available at the official website and you can download it from the given download link below click on the Download Python keyword. Download Python Since it is open-source, this means that source code is also available to the public. So you can download it, use it as well as share it.

2. **Easy to code**

Python is a high-level programming language. Python is very easy to learn the language as compared to other languages like C, C#, Javascript, Java, etc. It is very easy to code in the Python language and anybody can learn Python basics in a few hours or days. It is also a developer-friendly language.

3. **Easy to Read**

As you will see, learning Python is quite simple. As was already established, Python’s syntax is really straightforward. The code block is defined by the indentations rather than by semicolons or brackets.

4. **Object-Oriented Language**

One of the key features of Python is Object-Oriented programming. Python supports object-oriented language and concepts of classes, object encapsulation, etc.

5. **GUI Programming Support**

Graphical User interfaces can be made using a module such as PyQt5, PyQt4, wxPython, or Tk in Python. PyQt5 is the most popular option for creating graphical apps with Python.

6. **High-Level Language**

Python is a high-level language. When we write programs in Python, we do not need to remember the system architecture, nor do we need to manage the memory.

7. **Large Community Support**

Python has gained popularity over the years. Our questions are constantly answered by the enormous StackOverflow community. These websites have already provided answers to many questions about Python, so Python users can consult them as needed.

8. **Easy to Debug**

Excellent information for mistake tracing. You will be able to quickly identify and correct the majority of your program’s issues once you understand how to interpret Python’s error traces. Simply by glancing at the code, you can determine what it is designed to perform.

9. **Python is a Portable language**

Python language is also a portable language. For example, if we have Python code for Windows and if we want to run this code on other platforms such as Linux, Unix, and Mac then we do not need to change it, we can run this code on any platform.

10. **Python is an Integrated language**

Python is also an Integrated language because we can easily integrate Python with other languages like C, C++, etc.

11. Interpreted Language

Python is an Interpreted Language because Python code is executed line by line at a time. like other languages C, C++, Java, etc. there is no need to compile Python code this makes it easier to debug our code. The source code of Python is converted into an immediate form called bytecode.

12. **Large Standard Library**

Python has a large standard library that provides a rich set of modules and functions so you do not have to write your own code for every single thing. There are many libraries present in Python such as regular expressions, unit-testing, web browsers, etc.

13. **Dynamically Typed Language**

Python is a dynamically-typed language. That means the type (for example- int, double, long, etc.) for a variable is decided at run time not in advance because of this feature we don’t need to specify the type of variable.

14. **Frontend and backend development**

With a new project py script, you can run and write Python codes in HTML with the help of some simple tags <py-script>, <py-env>, etc. This will help you do frontend development work in Python like javascript. Backend is the strong forte of Python it’s extensively used for this work cause of its frameworks like Django and Flask.

15. **Allocating Memory Dynamically**

In Python, the variable data type does not need to be specified. The memory is automatically allocated to a variable at runtime when it is given a value. Developers do not need to write int y = 18 if the integer value 15 is set to y. You may just type y=18.

# Describe the role of predefined keywords in Python and provide examples of how they are used in a programming .

ANSWER - *Keywords * :   

#and	-  This is a logical operator which returns true if both the operands are true else returns false.

#or - This is also a logical operator which returns true if anyone operand is true else returns false.

# not -	This is again a logical operator it returns True if the operand is false else returns false.

#if -	This is used to make a conditional statement.

#elif -	Elif is a condition statement used with an if statement. The elif statement is executed if the previous conditions were not true.

#else	-Else is used with if and elif conditional statements. The else block is executed if the given condition is not true.

#for	- This is used to create a loop.

# while	- This keyword is used to create a while loop.

# break	- This is used to terminate the loop.

#as	- This is used to create an alternative.

#def-	It helps us to define functions.

#lambda	- It is used to define the anonymous function.

#pass	-This is a null statement which means it will do nothing.

#return -	It will return a value and exit the function.

#True	-This is a boolean value.

#False-	This is also a boolean value.

#try	- It makes a try-except statement.

#with -	The with keyword is used to simplify exception handling.

#assert -	This function is used for debugging purposes. Usually used to check the correctness of code

#class	- It helps us to define a class.

#continue	- It continues to the next iteration of a loop

#del	-It deletes a reference to an object.

#except	- Used with exceptions, what to do when an exception occurs

#finally	-Finally is used with exceptions, a block of code that will be executed no matter if there is an exception or not.

#from -	It is used to import specific parts of any module.

#global-	This declares a global variable.

#import-	This is used to import a module.

#in	-It’s used to check whether a value is present in a list, range, tuple, etc.

#is	-This is used to check if the two variables are equal or not.

#none	-This is a special constant used to denote a null value or avoid. It’s
#important to remember, 0, any empty container(e.g empty list) do not compute to None

#nonlocal -	It’s declared a non-local variable.

#raise	-This raises an exception.

#yield	-It ends a function and returns a generator.

#async-	It is used to create asynchronous coroutine.

#await-	It releases the flow of control back to the event loop.

#**EXAMPLES**
"""

import keyword
print(keyword.kwlist)

# True , False , or , and
True and False

True or False

True and True

False or False

True - False

a = (5 > 3 or 5 > 10 )

print (a)

b = (5 > 3 and 5 > 10)
print (b)

c = (5 < 2 | 2 > 1) # we can write in this way also
c

c = (5 > 2 & 2  > 1)
c

#while
x = 0
while x < 9 :
  print (x , "x is less than 9 ")
  x = x +1

#for
for x in range(0, 10):
  print(x)

for i in range (4):
  for j in range(4):
      print (  "*", end = " ")

  print()

#else , elif , if

a = 10
if a <= 10 :
  print ("a")

a = 2
if a >= 5 :
  print ("yes")
else :
  print("no")

MARKS = 70
if MARKS >= 90 :
  print ("grade A ")
elif 80 <= MARKS < 90 :
  print("grade B")
elif 65 <= MARKS < 80 :
  print ("grade C")
else :
  print ("not passed")

#None
a = None
print (a)
type(a)

#not
x = False
print (not False)

#break , continue
for i in range (0, 10):
  if i > 3 :
    break
  print(i)

for i in range (0, 10):
  if i == 5 :
    continue
  print(i)

#as , assert

import calendar as c

print(c.month_name[1])

x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:

assert x == "goodbye"

x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

class Person:
  name = "John"
  age = 36
print(Person.name)

p1 = Person() #Create an object named p1

print(p1.name)

def my_function():
  print("Hello from a function") # def keyword is used to create, (or define) a function.



my_function()

class MyClass:
  name = "John"
print(MyClass.name)
del MyClass

print (MyClass)

x = "hello goodmorning"
del x[0:4]  #str obj does not support item deletion
print(x)

x = ["apple", "banana", "cherry"]

del x[0]

print(x)

type(x)

x = "hello"

try:
  x > 3
except NameError:
  print("You have a variable that is not defined.")
except TypeError:
  print("You are comparing values of different type")

try:
  x = 1/0
except NameError:
  print("You have a variable that is not defined.")
except TypeError:
  print("You are comparing values of different type")
except:
  print("Something else went wrong")

try:
  x > 3
except:
  print("Something went wrong")

try:
  x > 3
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The try...except block is finished")

from datetime import time

x = time(hour=15)

print(x)

def myfunction():
  global x
  x = "hello"

myfunction()

#x should now be global, and accessible in the global scope.
print(x)

x = ["apple", "banana", "cherry"]

y = x

print(x is y)

x = lambda a : a + 10

print(x(5))

x = lambda a, b, c : a + b + c

print(x(5, 6, 2))

for x in [0, 1, 2]:
  pass

a = 33
b = 200

if b > a:
  pass

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

def myfunction():
  return 3+3

print(myfunction())

def myfunction(): #Statements after the return line will not be executed:
  return 3+3
  print("Hello, World!")

print(myfunction())

#Unlike the return keyword which stops further execution of the function,
 #the yield keyword continues to the end of the function.
 #When you call a function with yield keyword(s),
 # the return value will be a list of values, one for each yield.

def myFunc():
  yield "Hello"
  yield 51
  yield "Good Bye"

x = myFunc()

for z in x:
  print(z)

def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

# nonlocal keyword is used to work with variables inside nested functions,
#where the variable should not belong to the inner function.
#Use the keyword nonlocal to declare that the variable is not local.



"""**COMPARE AND CONTRAST MUTABLE AND IMMUTABLE OBJECTS IN PYTHON WITH EXAMPLES**

Mutable objects are those that allow you to change their value or data in place without affecting the object’s identity.
In contrast, immutable objects don’t allow this kind of operation. You’ll just have the option of creating new objects of the same type with different values.
Immutable objects are common in functional programming, while mutable objects are widely used in object-oriented programming.
Immutable Objects are of in-built datatypes like int, float, bool, string, Unicode, and tuple. In simple words, an immutable object can’t be changed after it is created.

Mutable and immutable objects are handled differently in Python. Immutable objects are quicker to access and are expensive to change because it involves the creation of a copy. Whereas mutable objects are easy to change.
The use of mutable objects is recommended when there is a need to change the size or content of the object.
Exception: However, there is an exception in immutability as well. We know that a tuple in Python is immutable. But the tuple consists of a sequence of names with unchangeable bindings to objects.

Example :
"""

# Python code to test that
# tuples are immutable

tuple1 = (0, 1, 2, 3)
tuple1 [0] = 5
print(tuple1)

# Python code to test that
# strings are immutable

message = "Welcome to my world "
message [0] = 'p'
print(message)

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

my_list.insert(1, 5)
print(my_list)

my_list.remove(2)
print(my_list)

popped_element = my_list.pop(0)
print(my_list)
print(popped_element)

my_dict = {"name": "Ram", "age": 25} #mutable i.e., we can make changes in the Dictionary.
new_dict = my_dict
new_dict["age"] = 37

print(my_dict)
print(new_dict)

my_set = {1, 2, 3}  ##mutable i.e., we can make changes in the Dictionary.

my_set.add(4)

print(my_set)



"""**Discuss the different types of operators in Python and provide examples of how they are used**

**ANSWER**
"""



"""Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

---



Arithmetic Operators in Python

---



Addition >> + >> adds two operands >>	x + y

Subtraction >> - >> subtracts two operands >> 	x – y

Multiplication >> * >> multiplies two operands	>> x * y

Division (float) >> /  >>  divides the first operand by the second	>> x / y

Division (floor) >> // >>  divides the first operand by the second	>> x // y

Modulus >> % >>  returns the remainder when the first operand is divided by the second	>> x % y

Power >> ** >> Returns first raised to power second	>> x ** y


"""

a = 9
b = 4
add = a + b

sub = a - b

mul = a * b

mod = a % b

p = a ** b

print(add)
print(sub)
print(mul)
print(mod)
print(p)

print(5/5)   #Float division
print(10/2)
print(-10/2)
print(20.0/2)

print(10//3)  # Floor division
print (-5//2)
print (5.0//2)
print (-5.0//2)

"""

---


**Comparison of Python Operators**

---

"""



"""Greater than " > " : True if the left operand is greater than the right :	x > y

"<"	Less than: True if the left operand is less than the right :	x < y

"=="	Equal to: True if both operands are equal: 	x == y

"!="	Not equal to : True if operands are not equal :	x != y

">="	Greater than or equal to : True if the left operand is greater than or equal to the right :	x >= y

"<=" :	Less than or equal to : True if the left operand is less than or equal to the right	: x <= y
"""

a = 20
b = 35

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

"""---


Logical Operators in Python

---

and	:Logical AND: True if both the operands are true	x and y

or:	Logical OR: True if either of the operands is true 	x or y

not :	Logical NOT: True if the operand is false 	not x
"""

a = True
b = False
print(a and b)
print(a or b)
print(not a)

"""---
Bitwise Operators in Python


---

&	Bitwise AND	x & y

|	Bitwise OR	x | y

~	Bitwise NOT	~x

^	Bitwise XOR	x ^ y

>> Bitwise right shift	x>>

<<	Bitwise left shift	x<<
"""

a = 10
b = 4
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

"""

---
Assignment Operators in Python


---


"""



"""=	>> Assign the value of the right side of the expression to the left side operand >>	x = y + z

+=  	>> Add AND : Add right-side operand with left-side operand and then assign to left operand	>> a+=b   >>  a=a+b

-= >>	Subtract AND : Subtract right operand from left operand and then assign to left operand	>> a-=b   >>   a=a-b

*=	>>  Multiply AND : Multiply right operand with left operand and then assign to left operand >>	a*=b   >>  a=a*b

/=  >> 	Divide AND : Divide left operand with right operand and then assign to left operand	a/=b  >>   a=a/b

%= >>	Modulus AND : Takes modulus using left and right operands and assign the result to left operand >>	a%=b  >>   a=a%b

//=	Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand >>	a//=b >>    a=a//b

**= >>	Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand >>	a**=b    >> a=a**b

&= >>	Performs Bitwise AND on operands and assign value to left operand	>>   
 a&=b   >>  a=a&b

|= >>	Performs Bitwise OR on operands and assign value to left operand	>>   
 a|=b   >>  a=a|b

^=	>> Performs Bitwise xOR on operands and assign value to left operand	a^=b   >>  a=a^b

>>=	Performs Bitwise right shift on operands and assign value to left operand	a>>=b     a=a>>b

<<=	Performs Bitwise left shift on operands and assign value to left operand	a <<=   >>   a= a << b
"""

a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

"""---


I**dentity Operators in** **Python**

---

is          True if the operands are identical

is not      True if the operands are not identical
"""

a = 10
b = 20
c = a

print(a is not b)
print(a is c)

"""---


**Membership Operators in Python**

---

in          :  True if value is found in the sequence

not in       : True if value is not found in the sequence
"""

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

"""**Explain the concept of type casting in Python with examples**"""



"""type Casting is the method to convert the Python variable datatype into a certain data type in order to perform the required operation by users. In this article, we will see the various techniques for typecasting. There can be two types of Type Casting in Python:

Python Implicit Type Conversion

Python Explicit Type Conversion
"""

# Python program to demonstrate
# implicit type Casting

# Python automatically converts
# a to int
a = 7
print(type(a))

# Python automatically converts
# b to float
b = 3.0
print(type(b))

# Python automatically converts
# c to float as it is a float addition
c = a + b
print(c)
print(type(c))

# Python automatically converts
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))

#Explicit Type Conversion in Python

a = 5
print (type(a))
n = float(a)

print(n)
print(type(n))

a = 5.9 #float

# typecast to int
n = int(a)

print(n)
print(type(n))

# int variable
a = 5

# typecast to str
n = str(a)

print(n)
print(type(n))

# string variable
a = "5"
b = 't'

# typecast to int
n = int(a)

print(n)
print(type(n))

print(int(b))

print(type(b))

# integer variable
a = 5
# string variable
b = 't'

# typecast to int
n = a+b

print(n)
print(type(n))

"""**How do conditional statements work in Python? Illustrate with examples**


Conditional Statements are statements in Python that provide a choice for the control flow based on a condition. It means that the control flow of the Python program will be decided based on the outcome of the condition.
"""

# if statement example
if 10 > 5:
    print("10 greater than 5")

print("Program ended")

# if..else statement example
x = 3
if x == 4:
    print("Yes")
else:
    print("No")

# if..else chain statement
letter = "A"

if letter == "B":
    print("letter is B")

else:

    if letter == "C":
        print("letter is C")

    else:

        if letter == "A":
            print("letter is A")

        else:
            print("letter isn't A, B and C")

# if-elif statement example
letter = "A"

if letter == "B":
    print("letter is B")

elif letter == "C":
    print("letter is C")

elif letter == "A":
    print("letter is A")

else:
    print("letter isn't A, B or C")

#while loop example >> conditional loops
x = 5
while x < 10:
    print(x)
    x += 1

#for loop example with condition
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)

"""Describe the different types of loops in Python and their use cases with examples.

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":  #Looping Through a String
  print(x)

fruits = ["apple", "banana", "cherry"]   #The break Statement >> Exit the loop when x is "banana":
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"] #Exit the loop when x is "banana", but this time the break comes before the print:
for x in fruits:
  if x == "banana":
    break
  print(x)

#The continue Statement >> With the continue statement we can stop the current iteration of the loop, and continue with the next:
#Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The range() Function
# range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)

for x in range(2, 6): #Using the start parameter:
  print(x)

#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

#Else in For Loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Nested Loops
#A nested loop is a loop inside a loop.

#The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#the pass Statement
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement

