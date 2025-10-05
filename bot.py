import os
import telebot
import time

BOT_TOKEN = os.environ['BOT_TOKEN']  # Только так!
bot = telebot.TeleBot(8362716922:AAGxYr0vajDXcOMIMlmLITvwEtetoesoOsU)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я работаю через GitHub! 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Вы сказали: {message.text}")

if __name__ == "__main__":
    while True:
        try:
            print("Бот запущен...")
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(10)
