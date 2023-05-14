# TelegramBot-GoogleBard
This bot is powered by the aiogram library using Google Bard.
## Installing dependencies
Create a virtual environment, install the required dependencies with `pip install -r requirements.txt`

## Google Bard Token
Go to https://bard.google.com/
- F12 for console
- Copy the values
- - Session: Go to Application → Cookies → __Secure-1PSID. Copy the value of that cookie.

![Application -> Cookies -> https://bard.google.com/ -> __Secure-1PSID](https://proghunter.ru/media/images/uploads/2023/05/14/568cbb5eca-uploaded-image.png) 

## Telegram Bot token

Now we need to create a bot in a telegram, this is done through **@BotFather**, start a dialogue and enter the command `/newbot`, select a name, be sure that the name contains the word: `Bot`, or through the underscore `_bot`

![Team example](https://proghunter.ru/media/images/uploads/2023/02/09/edaeddbca3-uploaded-image.jpg)

We get the key to access **API**, it is shaded in the screenshot.

## Launch Bot

- In the console, enter `py main.py`, and use it for our own purposes.

## Dialog with a bot

![Dialog screenshot 1](https://proghunter.ru/media/images/uploads/2023/05/14/256ffa2248-uploaded-image.png) 

![Dialog screenshot 2](https://proghunter.ru/media/images/uploads/2023/05/14/7709de8995-uploaded-image.png) 

Full article with images on my [website](https://proghunter.ru/articles/python-bot-powered-by-google-bard-neural-network-for-telegram)

## Proxy 

Without using a proxy, you may encounter the following error:

```
Google Bard encountered an error: b')]}\'\n\n38\n["wrb.fr",null,null,null,null,[9]]\n56\n["di",196," af.httprm",196,"5929433453807571131",4]\n25\n["e",4,null,null,131]\n'.
```
