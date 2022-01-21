import os
import shutil
from tabnanny import check

print(os.getcwd())
# getcwd = get current working directory
# os.mkdir('second1')

path1 = 'D:\\python!\\whitehat python\\class 99! saving files\\class99.py'

ans = os.path.exists(path1)

print(ans)
first, second  =  os.path.splitext(path1)

print(first, second)

print(os.listdir())


