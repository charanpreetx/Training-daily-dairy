# 25-06-2025.
# Python comments.
# "#" is single line comment.

"""This is Multiline 
# comments using double quotes."""

# '''This is multiline 
# comments using single quotes.'''

# # Python basics.
# x="Hello"   # String is a collection of characters.
# print(x)

# x=25        # integer
# print(x)

# x=25.5       # float
# print(x)

# z=True      # Boolean (True/False)
# print(z)


# # Variables: are created to store value. Variables are created When we assign any value to them.
# # Do not need to declare any datatype. We can change values of variables.
x=4
print(x)
x="Hello World"
print(x)

# Variable name.
# must start with letter or _.   # xyz, _xyz(Valid)  
# cannot start with number.   # 3xyz(not valid)
# only contain(A-z,0-9,_)   # xy23z, x_y
# case-sensitive. a and A both are different.
# no space between name.   # xy z

# # Three types of variable name.
# # camel case (myVariableName) (helloThisIsVariable)
# # pascal case (MyVariableName)
# # Snake case (my_variable_name)

# my_variable_name=34.5
# print(my_variable_name)
# print(type(my_variable_name))

# # # Assign multiple values to a multiple variable. no of variables should be equal to no of values.
# x,y,z=24,45,56
# print(x)
# print(y)
# print(z)

# # # # One value to multiple variables: 
# x=y=z="Single"
# print(x)
# print(y)
# print(z)

# Scope Local Global
# # Local variable: are created inside the function. can be used only inside the function.

# def functionname():     # Function defination.
#     statement

# functionname()     # Function calling.

# def func():
#     xx="local"
#     print(xx)
# func()
# # print(xx)

# # # global keyword.
# def func():
#     global xg
#     xg="local with global keyword"
#     print(xg)
# func()
# print(xg)

# # Global variable: are created outside the function
# xx="Global"
# def func():
#     print(xx)
# func()
# print(xx)

# # Datatypes: str, int, float, boolean, range, list, tuple, dict, set.
# # Python does not have character datatype. a single character is simply a string of length 1.
# "H" it is a string of length 1.
# s="Hello"  # "Hello world" 
# print(type(s))
# xyz=23
# f=2.4
# b=True/False
# list=["Hi","banana","cherry"]  
# tuple=("hi","cherry")
# dict={{"name":"Ajay","adress":"india"}}
# set={"Hi","this","set"}
# range(6)  , range(0,1,2,3,4,5)
# range(0,8)

# # Operators.
# # Arithmetic. 
# # Assignment. 
# # Comparison. 
# # Logical. 
# # Identity. 
# # Membership.

# # Arithmetic. +,-,/,*,%
# # X and y are operands.
# x=5
# y=3
# print("Addition",x+y)
# print("Subtraction",x-y)
# print("Multiplication",x*y)
# print("Division",x/y)
# print("Modulus",x%y)          # remainder

# # # Assignment.
# x=5
# print(x)
# x+=3         # 5+3=8  x=x+3
# print(x)
# x*=3         # 8*3=24  x=x*3
# print(x)

# # Comparison. 
# x=5
# y=3 
# print(x==y)  # Result True/False    
# print(x!=y)
# print(x>y)
# print(x<y)
# print(x>=y)
# print(x<=y)

# # Logical.  and(1,1=1)(1,0=0) or(1,1=1)(1,0=1) ,not
# x=4
# y=5
# z=6
# print(x>y and y<z)   #4>5 and 5<6   (0 and 1)=0/False
# print(x>y or y<z)    # 4>5 or 5<6   (0 or 1)=1/True
# print(not(x>y and y<z)) # not(4>5 and 5<6)   not(0 and 1)   not(0) will reverse the result and final result =1/True

# # Identity.  is
x=["apple","banana"]
y=["apple","banana"]
z=x
print(id(z))       # address of z is same as x.
print(id(x))
print(id(y))
print(x is z)                       
print( x is y)     # check address also                 
print(x==y)    # check value

# # Membership.  in, not in
x=["apple","banana"]
print("banana" in x)   # True/False
print("cherry" in x)                    
print("cherry" not in x) 
if "banana" in x:
 print("Banana is in list x")