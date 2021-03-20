__author__ = "Kristóf Kékesi"
__domain__ = "https://api.kekesi.dev/elements/v1/"
__version__ = "v1"

import io
import os
import json

# read elements.json
with io.open("elements.json", "r", encoding="utf8") as json_file:
	data = json.load(json_file)
	
	# making the folders using later
	try:
		os.makedirs(os.path.join(__version__, "covers"))
	except Exception as inst:
		print(inst)
	
	# looping through elements
	for index in range(0, len(data)):

		# making the folders using later
		try:
			os.makedirs(os.path.join(__version__, "element", str(index + 1), "isotope"))
		except Exception as inst:
			print(inst)

		# if element has isotope(s)
		if data[index]["isotopesSrc"]:
			with io.open(data[index]["isotopesSrc"], "r", encoding="utf8") as json_file:
				isotopeData = json.load(json_file)

				# looping through isotopes
				for innerIndex in range(0, len(isotopeData["isotopes"])):

					#making the folders using later
					try:
						os.makedirs(os.path.join(__version__, "element", str(index + 1), "isotope", str(innerIndex + 1)))
					except Exception as inst:
						print(inst)

					# saving isotopes individually
					with io.open(__version__ + "/element/" + str(index + 1) + "/isotope/" + str(innerIndex + 1) + "/data.json", "w",
								 encoding="utf8") as file:
						json.dump(isotopeData["isotopes"][innerIndex], file)

				# saving isotopes in one file
				with io.open(
						__version__ + "/element/" + str(index + 1) + "/isotope/data.json",
						"w",
						encoding="utf8") as file:
					json.dump(isotopeData["isotopes"], file)

			# reformat coverImage
			data[index]["coverImage"] = __domain__ + data[index]["coverImage"]
			
			# reformat isotopeSrc
			isotopesSrc = data[index]["isotopesSrc"].replace("isotopes", "isotope").split("/")
			isotopesSrc[-1] = "data.json"
			data[index]["isotopesSrc"] = __domain__ + "element/" + str(index + 1) + "/" + "/".join(isotopesSrc)

		# saving elements individually
		with io.open(__version__ + "/element/" + str(index + 1) + "/data.json", "w", encoding="utf8") as file:
			json.dump(data[index], file)

	# saving elements in one file
	with io.open(__version__ + "/element/data.json", "w", encoding="utf8") as file:
		json.dump(data, file)