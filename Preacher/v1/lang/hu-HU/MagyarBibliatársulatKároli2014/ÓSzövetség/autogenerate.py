import os

dirName = input("könyv rendszeri neve: ")
externalNum = input("fejezetek száma: ")

for num in range(int(externalNum)):
    os.system("mkdir " + dirName.replace("%num%", str(num+1)))