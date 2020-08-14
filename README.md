
# Fortnite-Api Discord
![Preview](https://i.ibb.co/Th3CzzN/fortnite-api-discord-final.gif)

Discord bot to get fortnite data from [Fortnite-Api.com](https://fortnite-api.com/) using discord.py!

**README en español** >>> [README_ES](https://github.com/BayGamerYT/Fortnite-Api-Discord/blob/master/README_ES.md)

# Usage
First you need to create an application in [Discord Developer Portal]([https://discord.com/developers/applications](https://discord.com/developers/applications)), make an Bot and copy the token.

* **Configuration:**
```css
Token                   : Your bot´s token. [str] Leave it blank to get it from .env (see below for more)
Prefix                  : Prefix for the commands. Leave it blank and it set automically to "f!" [str]
MaxSearchResults        : Max search results for "item" command [int]
Response lang           : Default language of Fortnite-Api responses. Leave it blank and it set automically to "en" [str]
Search lang             : Default language of Fortnite-Api requests. Leave it blank and it set automically to "en" [str]
bot_lang                : General bot lang (text). Leave it blank and it set automically to "en" [str]
```

* Configuration Options:

Api languages:
```
ar / de / en / es / es-419 / fr / it / ja / ko / pl / pt-BR / ru / tr / zh-CN / zh-Hant
```

Token:
You can get your bot token from .env file if you leave token blank.
The .env file need to be exactly like this:
```
Token=here_you_bot_token
```

Languages of the bot:
```
en / en
```
*You can provide translations in the support discord <3!

* **Commands:**
```css
item     : Get info for item name
brnews   : Show a embedded gif with the last BR News
cc       : Get info for requested creator code
```


**Please Note:**
If you are going to use this bot on a project I appreciate if you leave credits!