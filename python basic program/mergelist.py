# program to merge two list and sort it 
a=[]                                          #initialization of list 
c=[]
n1=int(input("enter no. of elements:"))
for i in range(1,n1+1):
    b=int(input("enter elements:"))             # enter elements in a list
    a.append(b)
n2=int(input("enter no. of elements:"))
for i in range(1,n2+1):
    d=int(input("enter elements:"))
    c.append(d)

new=a+c
new.sort()                                       #sort function is used to sort list in ascending orders
print("sorted list is :",new)