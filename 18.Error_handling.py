#Index Error:
try:
    list = [10,20,30] # 0 1 2
    n = int(input("Enter the index value"))
    print(list[n])
except IndexError :
 print("error:index out of range")
