#tuples can store the multiple data and data can't change
mytuple=("preeti","jyoti","saloni","preeti")
print(mytuple)  #can store duplicate values
print(type(mytuple))

#fetching values
print(mytuple[1])

#print all tuple values using for loop
for i in mytuple:
    print(i)
    
#dictionary (it can store multiple data in key value pair)
mydict={
    "name":"preeti sharma",
    "email":"bhardwajpreeti2102@gmail.com",
    "mobile":"9366666666"}
print(type(mydict))
print(mydict)
for i in mydict:
    print(mydict[i])
    
#to print specific value with the help of the key
print(mydict.get("email"))

#modification
mydict["name"]="preetii"
print(mydict)


