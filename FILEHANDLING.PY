#FILE HANDLING

#WITH FOR LOOP
file = open('input.txt','r')
for a in file:
    print(a)
#read()
file = open('input.txt',"r")
print(file.read())
#with statement
with open("input.txt")as file:
    data = file.read()
print(data)
# to read function creatain character
file = open('input.txt',"r")
print(file.read(5))
#readline()
file = open('input.txt',"r")
print(file.readline(8))
file.seek(0)
print(file.readline())
file.close()
# write the data to file
file = open("sujal.txt","w")
w = "hello"
l = ["this is first line"
     "this is second line"
     "this is third line"]
file.write(w)
file.writelines(l)
file.close()
