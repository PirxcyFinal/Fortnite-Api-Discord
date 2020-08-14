
# Fortnite-Api Discord
![Preview](https://i.ibb.co/Th3CzzN/fortnite-api-discord-final.gif)

Bot de Discord para conseguir información de los servidores de [Fortnite-Api.com](https://fortnite-api.com/) utilizando discord.py!

# Uso
Primero debes crear una aplicación en [Discord Developer Portal]([https://discord.com/developers/applications](https://discord.com/developers/applications)), crear un bot y copiar el token.

* **Configuración:**
```css
Token                   : El token de tu bot. [str] Déjalo en blanco para conseguirlo desde el archivo .env (mira abajo para más información)
Prefix                  : El prefijo para los comandos. Déjalo en blanco y se configurará automáticamente a "f!" [str]
MaxSearchResults        : Máximo número de resultados del comando "item" [int]
Response lang           : Idioma por defecto de las respuestas de Fortnite-Api. Déjalo en blanco y se configurará automáticamente en "en" [str]
Search lang             : Idioma por defecto de las solicitudes de Fortnite-Api. Déjalo en blanco y se configurará automáticamente en "en" [str]
bot_lang                : Idioma del bot en general (textos). Déjalo en blanco y se configurará automáticamente en "en" [str]
```

* Opciones de configuración:

Idiomas para la Api:
```
ar / de / en / es / es-419 / fr / it / ja / ko / pl / pt-BR / ru / tr / zh-CN / zh-Hant
```

Token:
Puedes conseguir el token desde el archivo .env
El archivo .env debe estar exactamente:
```
Token=aqui_el_token_de_tu_bot
```

Idiomas del bot:
```
en / es
```
*Puedes aportar traducciones en el discord de soporte <3!

* **Comandos:**
```css
item     : Consigue información para un ítem por nombre
brnews   : Muestra un gif en embed de las noticias del battle royale
cc       : Consigue información para el código de creador ingresado
```


**Nota:**
Si vas a utilizar este bot en un proyecto agradezco si dejas créditos!