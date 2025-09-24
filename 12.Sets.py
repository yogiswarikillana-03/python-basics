a = {1,2,3}
print(a)
a = {1,2,3,3,2,1,1,2}
print(a) #output {1,2,3}
#creating a set 
s1 = {1,2,3}
s2 = {10,12.5,"hello",True}
#Empty set 
s31 = {}
s3 = set()
print(type(s31))
#Accessing set
A = {"Rajinikant","snake king","uppendra"}
for role in A:
    print(role)
#Adding elements in sets:
S = {12,18,20}
S.add(25) # adds only single element in any postion
S.update([34,29]) #adds the multiple values in the set
print(S)  # {12,18,20,25,34,29,25}
# Deleting the elements in set 
S = {12,18,20,25,34,29,25}
S.remove(25) 
print(S)
#discard
S = {12,18,20,25,34,29,25}
S.discard(26) 
print(S)
#pop
S = {12,18,20,25,34,29,25}
S.pop() 
print(S)
#clear
S = {12,18,20,25,34,29,25}
S.clear() 
print(S)
#Mathematical operations in set:
A = {1,2,3}
B = {4,5,6}
print(A|B)
#Intersection "∩" "&":
A = 3
B = 4
print(A & B) #{3,4}
#Difference "-" = "-":
A ={1,2,3,4}
B = {3,4,5,6}
print(A - B)
print(B - A)
#Symmetric difference "△" = "^"
A ={1,2,3,4}
B = {3,4,5,6}
print(A^B)
print(B^A)
