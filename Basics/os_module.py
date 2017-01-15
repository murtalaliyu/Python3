import os

curDir = os.getcwd()    #get current working directory
print(curDir)

os.mkdir('newDir')      #make new 

import time

time.sleep(2)

os.rename('newDir', 'newDir2')

time.sleep(2)

os.rmdir('newDir2')     #remove directory
