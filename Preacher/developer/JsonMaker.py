import codecs
import os
import re

# Compatible with 
# - https://www.biblia.hit.hu
# - https://www.kingjamesbibleonline.org

pasteFile = "pasteFile.txt"
finalFolder = "final"

while True:
	create = codecs.open(pasteFile, "w", "UTF-8")
	create.close()
	os.system('cls')
	while True:
		print('Másold be az pasteFile.txt-be, majd nyomd meg az entert')
		input()
		break
	while True:
		with codecs.open(pasteFile, "r", "UTF-8") as f:
			if len(f.read()) == 0:
				os.system('cls')
				input('Üres fájl, továbblépéshez enter.')
			else:
				while True:
					os.system('cls')
					print("Írja be a könyvet (például 1Móz1)")
					book = input("")
					if book != "":
						bookSplit = re.split("0|1|2|3|4|5|6|7|8|9", book)
						bookSplitOrg = list(filter(None, bookSplit))
						
						book = book.replace(bookSplitOrg[0], bookSplitOrg[0].capitalize())
						
						break
				while True:
					print("Írja be fejezet számát (például 1)")
					number = input("")
					if number != "":
						break
				while True:
					os.system('mkdir ' + finalFolder)

					object = [
						'{',
						'   "meta": {',
						'   "type": "text",',
						#'   "name": "' + number + '. Fejezet"', # Hungarian
						'   "name": "Chapter ' + number + '"', # English
						'   },',
						'   "data": [',
					]

					read = codecs.open(pasteFile, "r", "UTF-8")
					num = 1
					for lines in read:
						lines = lines.strip().replace("\n", "").replace("", "-").replace("\"", "\\\"")
						try:
							num = int(lines)
						except:
							if lines.replace(" ", "") != "":
								if lines[:len(str(num))] == str(num):
									lines = lines[len(str(num)):]

								object.append('        {')
								object.append('            "type": "line",')
								object.append('            "value": "' + lines.strip() + '"')
								object.append('        },')
								num = num + 1
					object.pop()
					object.append('        }')
					object.append('    ]')
					object.append('}')
					read.close()

					path = "final/" + book + "_" + number + "/"

					os.system("mkdir final\\" + book + "_" + number)

					read = codecs.open(path + "data.json", "w", "UTF-8")
					for element in object:
						print(element, file=read)
					read.close()
					os.system('cls')
					input("JSON Legenerálva (Továbblépéshez Enter)")
					break
		break