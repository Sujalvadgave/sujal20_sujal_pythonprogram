#directory mangement

import os
import datetime as dt

#os.mkdir('E:/sujal')

print("string fromat",os.getcwd())
print("Bytefromat",os.getcwdb())

#os.rename("py","ty")

print("current dirctory",os.getcwd())
os.chdir("E:/sujal")

print("current directory",os.getcwd())
print(os.path.getsize('C:/py'))
print("files in current directory",os.listdir("c:/py"))

'''os.rmdir('E:/sujal')
div_list = os.listdir("C:/py")
if len(div_list)==0:
    print("directory is empty")'''



print("Last aecessed time",os.path.getatime("E:/sujal"))
print(" Last modified time",os.path.getmtime("E:/sujal"))
access_time = dt.datetime_CAPI(os.path.getatime("E:/sujal")).strftime("%y-%m-%d")
print(access_time)
