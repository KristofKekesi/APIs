var info = [
	{
		"meta-all": "Szövetségek",
		"meta": "Szövetség",
		"dir": "ÓSzövetség",

		"name": "Ó szövetség",
	}, {
		"meta-all": "Szövetségek",
		"meta": "Szövetség",
		"dir": "ÚjSzövetség",

		"name": "Új szövetség",
	}
]

document.getElementsByTagName("body")[0].innerHTML = JSON.stringify(info);