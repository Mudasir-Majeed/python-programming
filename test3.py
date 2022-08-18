# unpack a list
fruits= ["Apple", "Mango", "Orange"]
x,y,z=fruits
print(x)
print(y)
print(z)
# unpack another list
cellPhones=["Apple","Samsung","xiomi","MI","Nokia"]
print(cellPhones[-2])
print("*****************")
a,b,c,d,e=cellPhones
print(a)
print(b)
print(c)
print(d)
print(e)
# print() function
print("Python is awesome")
x="Python"
y="Is"
z="Awesome"
print(x,y,z)
# when you try to combine a string and a number with + you will get error
a=5
b="john"
#print(a+b)
print(a,b)
# Gloabal variables that are created outside of a function
x="awesome"
def fun():
    print("python is "+ x)
fun()
y="Mudasir"
z=8
def My_fun():
 print("Hello"+y)
   # print("Age is"+z)
 print("Age",z)
My_fun()
x="Awesome"
def fun1():
    x="fantastic"
    print("Python is"+x) # itis a local variable inside a function
fun1()
print("python is "+x)
# to use global varible inside a function use global keyword 
def fun2():
    global x
    x ="Fantastic"
   # print(x)

fun2()
print("Python is "+ x)
# also use global variable when you want to change the variable inside a function by using global keyword
x="awesome"
def fun3():
 global x
 x="fantastic"
fun3()
print("Python is" + x)
print(bool(0))
