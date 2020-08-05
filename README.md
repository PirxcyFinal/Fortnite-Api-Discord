
# Fortnite-Api Discord
![Preview](https://i.ibb.co/Th3CzzN/fortnite-api-discord-final.gif)

This is a base in python to get fortnite data from [Fortnite-Api.com](https://fortnite-api.com/) using discord.py commands framework!

# Usage
First you need to create an application in [Discord Developer Portal]([https://discord.com/developers/applications](https://discord.com/developers/applications)), make an Bot and copy the token.

* **Configuration:**
```css
Token                   : Your bot´s token [str]
Prefix                  : Prefix for the commands. Leave it blank and it set automically to "f!" [str]
MaxSearchResults        : Max search results for "item" command [int]
Api response lang       : Default language of Fortnite-Api responses. Leave it blanck and it set automically to "en" [str]
Api request lang        : Default language of Fortnite-Api requests. Leave it blanck and it set automically to "en" [str]
```

* Configuration Options:

Api languages:
```
ar / de / en / es / es-419 / fr / it / ja / ko / pl / pt-BR / ru / tr / zh-CN / zh-Hant
```



* **Commands:**
```css
item     : Get info for item name
brnews   : Show a embedded gif with the last BR News
cc       : Get info for requested creator code
```


**Please Note:**
If you are going to use this bot on a project I appreciate if you leave credits!