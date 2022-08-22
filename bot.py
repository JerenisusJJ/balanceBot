from cgitb import text
import subprocess
import threading
import time
import config
import telebot
import updateTableInfo
bot = telebot.TeleBot(config.tokenBot, "markdown", num_threads=3)
admin = [351153237, 393319148, 1500309956]


def foo():
    print(time.ctime())
    subprocess.run(["python3", "updateTableInfo.py"])
    threading.Timer(600, foo).start()


foo()

bot.set_my_commands([
    # telebot.types.BotCommand("/start", "Перезапуск бота"),
    telebot.types.BotCommand("/balance", "Запрос баланса"),
    # telebot.types.BotCommand("/stop", "Стоп")
])


@ bot.message_handler(commands=['start'])  # создаем команду
def start(message):
    if message.chat.id not in admin:
        bot.send_message(message.chat.id, 'Не дозволено')
    else:
        bot.send_message(message.chat.id, 'Чего изволите сударь?')


@ bot.message_handler(commands=['balance'])  # создаем команду
def balance(message):
    if message.chat.id not in admin:
        bot.send_message(message.chat.id, 'Не дозволено')
    else:
        bot.send_message(message.chat.id, updateTableInfo.updateTableInfo())
        print(message.chat.username)


bot.polling(none_stop=True)
