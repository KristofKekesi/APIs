var info = [
	{
		"meta": "MagyarBibliatársulatKároli2014",
		"dir": "MagyarBibliatársulatKároli2014",

		"name": "Biblia",
		"authors": "Magyar Bibliatársulat",
		"year": 2014,

		"en-EN": "Hungarian",
		"hu-HU": "Magyar",
	}, {
		"meta": "en-US",
		"dir": "en-EN",


		"en-EN": "English",
		"hu-HU": "Angol",
	}
]

document.getElementsByTagName("body")[0].innerHTML = JSON.stringify(info);