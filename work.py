import os
import shutil
# organising files in folder also creating folder one 
path1 = 'D:\\python!\\whitehat python\\class 99! saving files'

doesit = os.path.exists(path1)

if doesit :
    listoffile = os.listdir(path1)

print(listoffile)

for i in listoffile:
    
    valuename, extention = os.path.splitext(i)
    print(valuename, extention)
    if extention == '':
        continue
    elif (os.path.exists(path1+'/'+extention)) :
        shutil.move(path1+'/'+i,path1+'/'+extention+'/'+i)
    else :
        os.mkdir(path1+'/'+extention)
        shutil.move(path1+'/'+i,path1+'/'+extention+'/'+i)