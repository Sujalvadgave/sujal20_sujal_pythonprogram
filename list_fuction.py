# list function
L1 = [1,2,"HELLO",3.4]

print(type(L1))

print(L1[0:])
print(L1[:])
print(L1[2:4])
print(L1[1:4:2])
print(L1[-1])
print(L1[-3:-1])
L1[2] = 10
print(L1)
 
#repetation
L2 = [9,8,7,6,5]
l2 = L1*2
print(l2)

# concatination
L3 = L1+L2
print(L3)
print(len(L3))

# iterating
list1 = [3, 5, 7, 2, 4]  
for i in list1:  
    print (i)
#adding element in list
L4 = []
n = int(input("enter a number of element"))
for i in range(0,n):
    L4.append(input("enter element"))
# removing the element
for i in  L4:
    print(i,end="")
    L4.remove(i)
    print(L4)
#*********TUPLE FUNCTION**********
T1 =(1,2,3,4,5,6,7,8)
print(T1)
print(T1[0])
T1 = T1*3
print(T1)
c = T1.count(2)
print(c)
i = T1.index(3)
print(i)
#*********SET FUNCTION************
S1 = {1,2,3}
S2 = {2,3,4}
print(S1.intersection(S2))
print(S1.union(S2))
print(S1.symmetric_difference(S2))

S3 ={'a','b','c','d'}
S3.add(c)
print(S3)
S3.remove('b')
print(S3)
S3.pop()
print(S3)
#************DICTIONARY FUNCTION**************
D1 ={1:"HELLO",2:"HI",'a':"WELCOME"}
print(D1.keys())
print(D1.items())
print(D1.get('a'))
newD1 = D1.copy()
print(newD1)
print(D1.pop(1))
print(D1.popitem())
print(D1)
D2 = {4 : "welcome"}
D1.update(D2)
print(D1)
D1.clear()
print(D1)

D3 = {'a' 'b' 'c'}
D4 = dict.fromkeys(D3,1)
print(D4)






