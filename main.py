import requests
import telebot
from telebot import types

URL = 'https://pastebin.com/api/api_post.php'
TOKEN = ""
bot = telebot.TeleBot(TOKEN)
STATE_DICT = {}

USER_DATA = {
    'api_dev_key': '',
    'api_option': 'paste',
    'api_paste_code': '',
    'api_paste_name': '',
    'api_paste_expire_date': 'N',
    'api_results_limit': '100'
}

@bot.message_handler(commands = ['start'])
def start(message):
    chat_id = message.chat.id
    STATE_DICT[chat_id] = 'START'
    bot.send_message(chat_id, 'Bot ready to work!')


def start_work(message):
    chat_id = message.chat.id
    if message.text == 'paste':
        bot.send_message(chat_id, "Send me a paste:")
        STATE_DICT[chat_id] = 'PASTE'


def paste(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Select a name:")
    USER_DATA['api_paste_code'] = message.text
    STATE_DICT[chat_id] = 'NAME'


def name(message):
    chat_id = message.chat.id
    USER_DATA['api_paste_name'] = message.text
    commit(chat_id)
    STATE_DICT[chat_id] = 'COMMIT'


def commit(chat_id):
    request = requests.post(URL, data = USER_DATA)
    bot.send_message(chat_id, request)
    STATE_DICT[chat_id] = 'PASTE'


@bot.message_handler(func = lambda message: True)
def sfm(message):
    states = {
        'START': start_work,
        'PASTE': paste,
        'NAME': name,
        'COMMIT': commit,
    }
    chat_id = message.chat.id
    states[STATE_DICT[chat_id]](message)


if __name__ == "__main__":
    bot.polling(none_stop=False, interval = 0, timeout = 20)
