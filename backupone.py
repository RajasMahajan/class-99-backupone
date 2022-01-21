import os
import shutil

# create folder for backup
destinationforfolder = 'D:\\python!\\whitehat python\\class 99! saving files'
os.mkdir(destinationforfolder+'/'+'backup')

# copy and then past to backup
normalbackup = 'D:\\python!\\whitehat python\\class 99! saving files\\backup\\'

source = 'D:\\python!\\whitehat python\\class 99! saving files\\.py\\'

listoffile = os.listdir(source)
print(listoffile)
for i in listoffile:
    shutil.copy((source+i), normalbackup)


