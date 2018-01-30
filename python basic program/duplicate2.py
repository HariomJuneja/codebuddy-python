# program to remove duplicate elements from array


n=int(input("enter the no. of elements:"))      
a=[]                                               # initialization of list       

for i in range(1,n+1):                             
    elem=int(input("enter the elements:"))         # enter the elements in an array
    a.append(elem)	
b=set()	                                           # set function is used to remove duplicate elements from list
unique=[]
for x in a:
    if x not in b:
        unique.append(x)                          # append function is used to add element in list
        b.add(x)
print("non duplicate items:")		
		
print(unique)