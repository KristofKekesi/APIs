[*Back to APIs*](https://github.com/KristofKekesi/APIs#readme)
<p align="center">
   <img width="128" align="center" src="elements-api.svg"></p>
<h1 align="center">
  Elements API
</h1>

<img src="https://img.shields.io/badge/Contributors-1-blue.svg" alt=""> [![Discord](https://img.shields.io/discord/639186082214445116.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/7URAMuc)

## Contributors <img src="https://img.shields.io/badge/1-blue.svg" alt="">
* _[Programming]_  - [__Kristóf Kékesi__](https://github.com/KristofKekesi)
 
## Contacts [![Discord](https://img.shields.io/discord/639186082214445116.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/7URAMuc)

<table>
 <tr><td>
  Discord:
 </td><td>
  https://discord.gg/7URAMuc
 </td></tr>
 <tr><td>
  mail:
 </td><td>
  kristofkekesiofficial@gmail.com
 </td></tr>
</table>

## Documentation

#### Get all elements
```http
GET https://api.kekesi.dev/Elements/v1/element/data.json
```

#### Get specified element
```http
GET https://api.kekesi.dev/Elements/v1/element/[ELEMENTSNUMBER]/data.json
```

#### Get all isotopes
```http
GET https://api.kekesi.dev/Elements/v1/element/1/isotope/data.json
```

#### Get all isotopes
```http
GET https://api.kekesi.dev/Elements/v1/element/1/isotope/[ISOTOPENUMBER]/data.json
```
