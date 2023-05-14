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

Article with images on [my site](https://proghunter.ru/articles/python-bot-powered-by-google-bard-neural-network-for-telegram)
