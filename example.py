import requests
import telebot

url = 'https://pastebin.com/api/api_post.php'
TOKEN = "1473852862:AAEx-Pzcne5qtZDy-FOJXa8E7wDN-gQamk8"
tb = telebot.TeleBot(TOKEN)

@tb.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    user_data = {
        'api_dev_key': 'PthjTNm8B_jsY9z_R9MQgsgkXmOnb20I',
        'api_option': 'paste',
        'api_paste_code': message.text,
        'api_paste_name': "My New",
        'api_paste_expire_date': 'N',
        'api_results_limit': '100'
    }
    r = requests.post(url, data= user_data)
    tb.send_message(message.chat.id, r)


if __name__ == "__main__":
    tb.polling(none_stop=False, interval=0, timeout=20)
 