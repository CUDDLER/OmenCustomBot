import config
import telebot

bot=telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def command_handler(message):
    keyboard_start = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Начать", callback_data="start_config")
    keyboard_start.add(callback_button)
    bot.send_message(message.from_user.id, 'Привет, ' + str(message.chat.first_name) + ', это бот-конфигуратор OmenBoyzCustom \n'
                                           'Я помогу тебе сделать именно тот дизайн, который ты хочешь!\n '
                                           'Жми "Начать"')

@bot.message_handler(commands=['help'])
def command_handler(message):
    keyboard_start = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Начать", callback_data="")
    keyboard_start.add(callback_button)
    bot.send_message(message.from_user.id, 'Доступные команды:'
                          '/start — Запуск бота'
                          '/help — Помощь'
                          '/sources — Ресурсы OmenBoyz')

@bot.message_handler(commands=['sources'])
def command_handler(message):
    keyboard_url = telebot.types.InlineKeyboardMarkup()  # resize_keyboard="False"
    callback_button_vk = telebot.types.InlineKeyboardButton(url="https://vk.com/omenboyzapparel", text="ВК")
    callback_button_inst = telebot.types.InlineKeyboardButton(url="https://instagram.com/omenboyz", text="Inst")
    callback_button_instcustom = telebot.types.InlineKeyboardButton(url="https://vk.com/omenboyzcustoms", text="ВК Custom")
    callback_button_vkcustom = telebot.types.InlineKeyboardButton(url="https://instagram.com/omenboyzcustoms", text="Inst Custom")
    keyboard_url.add([[callback_button_vk, callback_button_vkcustom],
                      [callback_button_instcustom, callback_button_inst]])

    bot.send_message(message.from_user.id, 'Ниже представлены наши сети, тебя там ждут :)', reply_markup = keyboard_url)

@bot.message_handler(content_types=["text"]) #Старт бота для сообщений
def command_handler(message):
    #try:
    #    return
    if message.text == "/config":
        bot.reply_to(message, 'Начала конфигуратора')
        return
   # except Exception as error:
   #     print("Excepcion in forward handler. Info: {}".format(error))

if __name__ == '__main__':
    bot.polling(none_stop=True)
