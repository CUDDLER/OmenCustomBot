import config
import telebot

bot=telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"]) #Старт бота
def command_handler(message):
    if message.text == 'Привет' or '/start':
        keyboard_start = telebot.types.InlineKeyboardMarkup()
        callback_button = telebot.types.InlineKeyboardButton(text="Начать", callback_data="test")
        keyboard_start.add(callback_button)
        bot.send_message(message.chat.id, "Привет, " + str(message.chat.first_name) + ", это бот-конфигуратор <b>OmenBoyzCustom</b> \n"
                                         "Я помогу тебе сделать именно тот дизайн, который ты хочешь!\n "
                                         "Жми <b>Начать</b>", reply_markup=keyboard_start, parse_mode=telebot.ParseMode.HTML )
    elif message.text == 'Помощь' or '/help':
        bot.send_message(message.chat.id, 'Чем тебе помочь?')

def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
