var info = [
	{
		"meta": "hu-HU",
		"dir": "hu-HU",

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