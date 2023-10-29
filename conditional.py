#CONDITIONAL STATEMENT
# USING IF-ELSE STATEMENT
i = int(input("enter a number"))
if (i < 15):
	print("i is smaller than 15")
	print("i'm in if Block")
else:
	print("i is greater than 15")
	print("i'm in else Block")
print("i'm not in if and not in else Block")

#check even or odd statement
#USING IF-ELSE STATEMENT
print("******** TO CHECK EVEN OR ODD ***********")
a = int(input("enter a number"))

if(a%2==0):
    print(a,"is a even number")
    print("i am in if block")
else:
    print(a,"is a odd number")
    print("i am else block")
#CHECK GREATEST OF 3 NUMBER
#USING if-elif-else statement

print("********* TO CHECK GREATEST OF THREE NUMBER************")

x=(int(input("enter a number")))
y = (int(input("enter second number\n")))
z= (int(input("enter third number\n")))
if(x>y and x>z):
    print(x,"is greatest number")
elif(y>z and y>x):
    print(y,"is greatest number")
else:
    print(z,"is greatest number")

#conditional loop
#for loop
l = ["first",1,2,0]
for i in l:
    print(i)
#continue
l=["dypcet"]
for l in "sujal":
    if(l=='e'or l=='p'):
       continue
print("letter",l)
#break
for l in "dypcetkolhap":
   if(l=='e' or l=='p'):
        break
print("letter",l)
#pass
for l in "dypcet":
    pass
print("letter",l)
#while loop
count = 0
while count<3:
    count = count+1
    print("hello")
a = [1,2,3,4,5,6]
while(a):
    print(a.pop())
    print(a)
#else with while
#count = 0
#while count<5:
    #print(count)
  #  count+1
#else:
# print(count)
#map function
x, y = input("Enter two values: ").split()
#multiple input for list
l = list()
a= int(input("enter list size"))
print("enter the element")
for i in range(0,a):
        l.append(int(input()))
        print(l)
#multiple input for set
l = set()
c= int(input("enter the size of set"))
print("enter the element")
for i in range(0,c):
        l.append(int(input()))
        print(l)





    
