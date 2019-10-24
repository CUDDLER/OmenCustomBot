import telebot
from os import environ
import params

bot = telebot.TeleBot(environ['token'])

@bot.message_handler(commands=['start'])
def start_handler(message):
    keyboard_start = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text='Начать', callback_data="start_config")
    keyboard_start.add(callback_button)
    user = message.chat.first_name
    start_mes = message_all(user)
    bot.send_message(message.from_user.id, start_mes)

@bot.message_handler(commands=['help'])
def help_handler(message):
    keyboard_start = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text='Начать', callback_data="")
    keyboard_start.add(callback_button)
    bot.send_message(message.from_user.id, params.help_message)


@bot.message_handler(commands=['sources'])
def sources_handler(message):
    keyboard_url = telebot.types.InlineKeyboardMarkup()  # resize_keyboard="False"
    callback_button_vk = telebot.types.InlineKeyboardButton(url="https://vk.com/omenboyzapparel", text='ВК')
    callback_button_inst = telebot.types.InlineKeyboardButton(url="https://instagram.com/omenboyz", text='Inst')
    callback_button_instcustom = telebot.types.InlineKeyboardButton(url="https://vk.com/omenboyzcustoms",
                                                                    text='ВК Custom')
    callback_button_vkcustom = telebot.types.InlineKeyboardButton(url="https://instagram.com/omenboyzcustoms",
                                                                  text='Inst Custom')
    keyboard_url.add(callback_button_vk, callback_button_vkcustom,
                     callback_button_instcustom, callback_button_inst)
    print(message.chat.first_name)
    bot.send_message(message.from_user.id, 'Ниже представлены наши сети, тебя там ждут :)', reply_markup=keyboard_url)





# except Exception as error:
#     print("Excepcion in forward handler. Info: {}".format(error))
@bot.message_handler(content_types=['text'])  # Старт бота для сообщений
def text_handler(message):
    # try:
    #    return
    if message.text == "/config":
        bot.reply_to(message, 'Начала конфигуратора')
        return



if __name__ == '__main__':
    bot.polling(none_stop=True)
