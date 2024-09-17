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

#oops
#class and object

class Preeti:   #class name in uppercase
    age=20
    print("hello")
    
#create object and pass class properties
preeti=Preeti()
print(preeti.age)

class agecalculator:
    birthyear=int(input("enter the birthyear"))
    currentyear=int(input("enter the current year"))
    Age=currentyear-birthyear

age=agecalculator()
print(age.Age)


#method overloading 
#def age(dob):
    #print(dob)
    
def age(dob,name):
    print(dob,name)
#x=age("1 dec 2003")
y=age("17 sep 2024","preeti")


    



