import telebot
import os
from dotenv import load_dotenv


def main():
    load_dotenv()

    print("LOADED TOKEN =", os.getenv("TOKEN"))

    bot = telebot.TeleBot(os.getenv("TOKEN"))

    @bot.message_handler(func=lambda a: True)
    def echo(a):
        bot.reply_to(a, a.text)

    print("launch")
    bot.infinity_polling()


if __name__ == "__main__":
    main()
