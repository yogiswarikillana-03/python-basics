import Numpy as np
#Creating an array with numpy:
#1D Array:
A1D = np.array([1,2,3,4,5])
print(A1D)
#2D Array:
A2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A2D)

a = np.array([1,2,3,4,5])
print(a.ndim)
print(A2D.ndim)
#shape
print(A1D.shape)
print(A2D.shape)
#size
print(A2D.size)
#dtype
print(A2D.dtype)

#2.creating an array with numpy
#zeros:
print(np.zeros(6))
#ones
print(np.ones(6))
#arrange:
print(np.arange(1,11,1)) #1 2 3 4 5 6 7 8 9 10
print(np.arange(0,11,2)) #0 2 4 6 8 10
print(np.arange(1,11,2)) #1 3 5 7 9
#linspace:
print(np.linspace(0,1,3)) #0 0.5 1
#mathematical operations:
A = np.array([1,2,3,4,5])
L = [1,2,3,4,5]
print(A+6)
print(A-6)
print(A*6)
print(A/6)
print(A//6)
print(A**6)
AA = []
for i in A:
    AA.append(i+6)
    print(AA)
#Aggregate Functions:
A = np.array([1,2,3,4,5])
#sum():
print(np.sum(A)) #15
#mean():
print(np.mean(A)) #3
#max():
print(np.max(A)) #5
#min
print(np.min(A)) #1
#median
print(np.median(A)) #3.0
#std:
print(np.std(A))
#cumprod:
print(np.cumprod(A)) #[1  2  6  24  120]
#matrix operations:
Mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
Mat2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(Mat1+Mat2)
print(Mat1**2)
print(Mat1*Mat2)
#dot:
print(np.dot(Mat1,Mat2))
#Transpose:
print(np.transpose(Mat1))
