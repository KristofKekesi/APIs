import os
os.system("title X-launch")
os.system("cls")
list = []
filename = input(" FILE: ")
read = open(filename, 'r')
for line in read:
	list.append(line.replace("\n", ""))
	if "//x-src" in line:
		oldfile = line.split()[1]
read.close()
while True:
	os.system("cls")
	print(" ../ = Back")
	print("   / = Up")
	print(" https:// = for web")
	print("\n OLD LINK:", oldfile, sep=" ")
	newfile = input(" NEW LINK: ")
	if newfile != "":
		break
	else:
		print("\n Please write the new link!")
		input(" />:")
while True:
	os.system("cls")
	print("---------------------------------------------------------------")
	print("", oldfile, "->", newfile, sep=" ")
	print("---------------------------------------------------------------")
	print(" Would you like to save", newfile, sep=" ")
	print("\n 1 Yes")
	print(" 2 No")
	save = input("\n />: ")
	try:
		save = int(save)
		if save == 1 or save ==2:
			break
		else:
			print(" Please wirte a correct number!")
			input(" />:")
	except ValueError:
		print(" Please write a number!")
		input(" />:")
if save == 1:
	write = open(filename, "w")
	for line in list:
		if "//x-src" in line:
			line = "		onload=\"window.open(' " + newfile + " ', '_top')\" //x-src"
			print(line, file=write)
		else:
			nothing = None
			print(line, file=write)
	write.close()