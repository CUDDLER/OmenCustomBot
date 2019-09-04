import config
import telebot

bot=telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def command_handler(message):

    keyboard_start = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Начать", callback_data="test")
    keyboard_start.add(callback_button)
    bot.reply_to(message, 'Привет, ' + str(message.chat.first_name) + ', это бот-конфигуратор OmenBoyzCustom \n'
                                                                 'Я помогу тебе сделать именно тот дизайн, который ты хочешь!\n '
                                                                 'Жми "Начать"')

@bot.message_handler(content_types=["text"]) #Старт бота для сообщений
def command_handler(message):
    print(message.text)
    if 'Помощь' or '/help' in message.text:
        bot.reply_to(message, 'Чем тебе помочь?')
        return
def help_handler(message):
    if 'Конфигуратор' or '/config' in message.text:
        bot.reply_to(message, 'Начала конфигуратора')
    bot.send_message(message, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
