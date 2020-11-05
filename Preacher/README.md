[*Back to APIs*](https://github.com/KristofKekesi/APIs#readme)
<h1 align="center">
  Preacher API
</h1>

<img src="https://img.shields.io/badge/Contributors-1-blue.svg" alt=""> [![Discord](https://img.shields.io/discord/639186082214445116.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/7URAMuc)

## Contributors <img src="https://img.shields.io/badge/1-blue.svg" alt="">
* _[Programming]_  - [__Kristóf Kékesi__](https://github.com/KristofKekesi)
* _[JSON Formatting]_ - [__Kristóf Kékesi__](https://github.com/KristofKekesi), [__Klári Bory__](https://www.instagram.com/boryklara/)
 
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

### Types of json files
The API is made up by four types of json files.
- Languages
- Language
- Book
- Folder
- Text

Each of these has their unique required parameters.
The directory tree is build up by the four types. Every types are there for once, except the type folder. Only book and folder can contain type folder directories inside them.

### Parameters
#### Languages
- meta
  - type <required> [String] ("languages")
  - url <required> [String] (url - domain)
- data
  - code <required> [String] (eg.: en-EN)
  - dir <required> [String]
  - en-EN <required> [String]
  - hu-HU <required> [String]
#### Language
- meta
  - type <required> [String] ("language")
  - url <required> [String] (url - domain)
- data
  - dir <required> [String]
  - name <required> [String]
  - authors <required> [String] (author(s) of the book)
  - en-EN <required> [String]
  - hu-HU <required> [String]
#### Book
- meta
  - type <required> [String] ("book")
  - url <required> [String] (url - domain)
  - name <required> [String]
  - cover <required> [String] (path to img - url)
  - hidden <required> [Bool]
  - finished <required> [Bool]
  - exclusice <required> [Bool]
- data
  - dir <required> [String]
  - name <required> [String]
  - description <required> [String]
#### Folder
- meta
  - type <required> [String] ("folder")
  - url <required> [String] (url - domain)
  - name <required> [String]
- data
  - dir <required> [String]
  - name <required> [String]
  - description <required> [String]
#### Text
- meta
  - type <required> [String] ("text")
  - name <required> [String]
- data
  - type <required> [String] ("title&num" - title then number / "sub" - subtitle / "line" - paragraph / "break" - line break)
  - value <required> [String]
