list1 = [10,20,30,40,50]
fruits = ["apple,mango,banana"]
list2 = [10.1,20.2,30.3,40.4,50.5]
list3 = [True,False,True,True]
list4 = [10,20.5,"hello",True,"False"] #multi datatype values.
#output
print(list4)
list1 = [10,20,30,40]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[-1])
print(list1[-2])
print(list1[-3])
print(list1[-4])
slc1 = ["PSPK","BOB","Balayya","Prabhas"]
print(slc1[:3])
print(slc1[1:4])
print(slc1[-3:])
kalkicast = ["Prabhas","Kamal h","Amitha bachan","Deepika p","Ssr"]
kalkicast.append("Deesha patani")
print(kalkicast)
kalkicast.insert(2,"vijay devarakonda")
print(kalkicast)
kalkicast.extend(["Anudeep","Mrunal thakur"])
print(kalkicast)
kalkicast.insert(5,"Brahmanandham")
print(kalkicast)
kalkicast.remove("Mrunal thakur")
print(kalkicast)
kalkicast.pop(7)
print(kalkicast)
kalkicast.clear()
print(kalkicast)
kalkicast = ["prabhas","Kamal h","Amitha bachan","Deepika p","ssr"]
kalkicast[1] = "Sandeep R V"
print(kalkicast)
a=[1,2]
b=[3,4]
c=a+b
print(c)
a=[1,2]
n=int (input("Enter the n value"))
b=a*n
print(b)
#Searching and checking
a = [2,4,6,8,8,8,10,12,14]
cnt=0
if 2 in a:
    print("Yes item is present in the list")
print(3 not in a)
#index
print(a.index(8))
#count
print(a.count(8))
for i in range(10):
    if i == 8:
        cnt = cnt + 1
print(cnt)
st = [25,12,5,31,13,18,7,45,8,55,68]
#AO = 5,7,8,12,13,18,25,31,45,55,68
st.sort()
print(st)
#DO = 68,55,45,31,25,18,13,12,8,7,5
st.reverse()
print(st)
#copying
Frd1 = ["A","C","D","A","D","B","B","C","C","A","A"]
Frd2 = Frd1.copy()
print(Frd2)
#Frd2[2] = "B"
print(Frd2)
#Multiple value using input data to the list 
a = input("enter the multipe values:").split()#10 20 30 40 50
print(a) #['10','20','30','40','50']
#list1 = [10,20,30,40,50]
cars =  ["thar", "jaguer","audi","bmw"]
for cars in cars:
    print("cars=" , cars)
#using index with for loop:
    print(len(cars)) #4
for i in range(0,5):
    print(i)
#Adding elements using for loop
#list1 = "thar","jaguer","audi","bmw"
list1 = []
for i in range (0,4):
    #list1 = "thar","audi","jaguer","bmw"
    list1.append("thar")
    print(list1)
    for i in range(0,n): # i 0 i
        a = input("enter the list values")
        list1.append(a)
        print(list1)
        list1 = [10,20,30,40,50]
        sum = 0#10
        for i in list1: #10 20 30 40 50 
            sum = sum + i #10
            print(sum) 
    #convert ["p","y","t","h","o","n"] to python
    list1 = ["y","t","h","o","n"]
    word = "p"
    for i in list1: #ython
        word = word + i 
        print(word)
#minimum and maximum
list1 = [7,10,12,18,17,23,31,45,227,229]
list1.sort()
# 52,7,10,12,18,17,23,31,45,227,229
# 0  1  2  3  4  5  6  7  8  9
print(list1)
#print("maximum of list:",list1[9])
#print("minimum of list:",list1[0])  
list1 = [52,7,12,18,17,23,31,45,227,229]
max1 =list1[0] #229
min1 = list1[0] #7
#searching for an element in a list
a = [2,4,6,8,10,12,14]
if 2 in a:
    print("yes item is present in the list")
Names = ["Mallareddy sir","modi sir","rahul gandhi"]
searching_name = input("enter the name to be found ")
for i in Names:
    if searching_name == i:
        found = True
if found:
         print("Yes")
else:
    print("No")
#count even and odd numbers
numbers = [7,10,18,17,12,31,45,23,227,229]
#o = 7
#e = 3
evn_cnt = 0
odd_cnt = 0
for i in range (len(numbers)):
    if numbers [i]%2 == 0:
     evn_cnt += 1
    else:
        odd_cnt += 1
print("Number of even numbers are:",evn_cnt)
print("Number of odd numbers are:",odd_cnt)
#Reversing a list without reverse
list1 = [7,10,12,18,17,23,31,45,227,229] # 1 = 10
#ind =   0  1  2  3  4  5  6  7  8  9
l = len(list1)
r_list = []
for i in range(1-1,-1,-1):
    r_list.append(list[i])
    print(r_list)
#Removing all negative numbers using loop # = (2,30,45,23,72,7)
numbers = [-56,-9,2,-8,-30,45,23,-19,72,-55,-18,7,0]
positive_list = []
for i in range(len(numbers)):
    if numbers[i] > 0:
        positive_list.append(numbers[i])
print(positive_list)
#Multiply each element in the list 
numbers = [-56,-9,2,-8,-30,45,23,-19,72,-55,-18,7,0]
m = int(input("Enter the number to be miltiplied:"))
After_multiplication = []
for i in numbers:
    After_multiplication.append(i*m)
print(After_multiplication)



 








