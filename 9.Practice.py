#Area of Triangle
height = int(input("Enter the height value: "))
base = int(input("Enter the base value: "))
AOT = 1/2*height*base
print(AOT)
#finding square and cube of a number
a = int(input("Enter a value"))
square = a**2
cube = a**3
print(square)
print(cube)
#km -> m, m ->cm,
dis = 25#m
km = dis/1000
m =dis*1000
m1 = dis/100
cm = dis*100
miles = dis*1.6

#find the number whether it is even or odd 
#Even = 0,2,4,6,8,10......
#Odd = 1,3,5,7,9.......
num = int(input("Enter num:"))
if num%2==0:
        print("Number is even")
else :
        print ("Number is odd")
#Leap year or not
year = int(input("Enter the year: "))
if (year%4==0 and year%100!=0) or year%400==0:
        print("it is a leap year")
else:
    print("it is not leap year")
#Average of all numbers in the list
numbers = [10,20,30,40,50]
sum_val = 0
count = 0
for num in numbers:
       sum_val += num
       count += 1
average = sum_val/count
print(average)



    

    

