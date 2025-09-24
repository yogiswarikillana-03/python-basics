#Functions:
def greet():
    print("Hello world")
greet()
greet()
greet()
greet()
greet()
name = "Yogiswari"
rollno = "D3"
print("hello",name)

#Types of functional arguments:
#A.positional arguments:
def greet(rollno,name): #step 2 values store
    print("hello",name,"your rollno is",rollno)
greet(name="yogiswari",rollno="D3")

#scope of the variable:
x = 10 #global variable
def var1():
    y = 5 #local variable
    print("inside var1 function", x,y)
var1()
def var2 ():
    print("inside var2 function", x)
var2()
print("outside function",x)

#Lambda function:
#normal function
def sqe(a):
    print(a*a) #25
sqe(5)
#Lambda function:
squ = lambda a:a*a
print(squ(5)) #25

# factorial
#5! = 5*4*3*2*1
def factorial(fact)
    fact = 1 #120
    for i in range(5,0,-1):#5 4 3 2 1
        














