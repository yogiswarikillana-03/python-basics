coordinates = ("x","y")
My_tuple = (10,20,30)
print(My_tuple)
print(type(My_tuple))
#Tuple with a same element
a = 10 #Int
print(type(a))
b = [10] #List
print(type(b))
c = (10,) #Tuple
print(type(c))
My_tuple = (10,20,30)
print(My_tuple)
print(type(My_tuple))
#Accessing elements:
#Tuple uses index values to access an element.
A = (10,20,30,40)
#i    0  1  2  3  
#i   -4 -3 -2 -1
print (A[0]) #10
print(A[1]) #20
print(A[2]) #30
print(A[3]) #40
print(A[-1]) #40
print(A[-2]) #30
print(A[-3]) #20
print(A[-4]) #10

#slicing the tuple:
#([start index:end index])
A = (10,20,30,40)
#i    0  1  2  3  
#i   -4 -3 -2 -1
print(A[1:3]) #20 30 40
print(A[:2])  #10 20 30
print(A[-3:-1]) #40 30 20

#Nested Tuple:
T = (10,(20,30,),(40,50))
#i    0     1       2
print(T[2][1])
