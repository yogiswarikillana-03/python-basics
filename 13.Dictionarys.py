My_dict = {
     "key1":"value1",
     "key2":"value2",
     "key3":"value3",
     "key4":"value4"
}
print(My_dict)
#characteristics of dictionary:
#Unique keys
A = {"n":"Yogiswari","n":"Honey"}
print(A) # "n1" :"Yogiswari" 

#creating dictionary
#normal dictionary:
BioData = {
     "Name":"Yogiswari",
     "Roll.No":"D3",
     "Branch" :"CSM AI&ML",
     "Place" : "Hyderabad"
}
#Dictionary using constructer:
BioData1 = dict(Name = "Yogiswari",RollNo = "D3",Branch = "CSM AI&ML",Place = "Hyderabad")
print(BioData1)
#Empty Dictionary:
E_D = {}

#Accessing the Dictionary:
BioData = {
     "Name":"Yogiswari",
     "Roll.No":"D3",
     "Branch" :"CSM AI&ML",
     "Place" : "Hyderabad"
} 
print(BioData["Name"])
print(BioData["Roll.No"])
print(BioData["Branch"])
print(BioData["Place"]) 
#Using get() method:
print(BioData.get("Name"))
print(BioData.get("Roll.No"))
print(BioData.get("Branch"))
print(BioData.get("Place"))
print(BioData.get("Age"))
#Adding and updating :
BioData = {
     "Name":"Yogiswari",
     "Roll.No":"D3",
     "Branch" :"CSM AI&ML",
     "Place" : "Hyderabad"
} 
#pop(): removes the key value
BioData.pop("Name")
print(BioData)
BioData.pop("Roll.No")
print(BioData)
BioData.pop("Branch")
print(BioData)
BioData.pop("Place")
print(BioData)
BioData.clear()
print(BioData)

#Dictionary methods:
BioData = {
     "Name":"Yogiswari",
     "Roll.No":"D3",
     "Branch" :"CSM AI&ML",
     "Place" : "Hyderabad"
} 
print(BioData.keys())
print(BioData.values())
print(BioData.items())

#updating
BioData.update({"Place":"Hyderabad","Branch":"CSM AI&ML"})
 
#Loops for dictionary
for i in BioData.values():
    print(i)
#Loops for dictionary:
L = [10,20,30,40,50]
for i in range (0,5):
     print (L[i])

BioData = {
     "Name":"Yogiswari",
     "Roll.No":"D3",
     "Branch" :"CSM AI&ML",
     "Place" : "Hyderabad"
} 
for i in BioData.items():
     print(i)
for i in BioData.keys():
     print(i)

#Nested Tuple:
T = (10,(20,30,),(40,50))
#i    0     1       2
print(T[2][1])

# Nested Dictionary
students = {
      "s1":{"Name":"Yogiswari","RollNo":"D3"},
      "s2":{"Name":"Mehraj","RollNo":"J2"}
}
print(students["s1"])
print(students["s2"])
print(students["s1"]["Name"])
print(students["s2"]["Name"])
print(students["s1"]["RollNo"])
print(students["s2"]["RollNo"])

