import config
import telebot


bot=telebot.TeleBot(config.token)

@bot.message_handler(commands=['start']) #Старт бота
def start_handler(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Начать", callback_data="test")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, 'Хай', reply_markup=keyboard)
#Привет, '+ str(user.first_name) + ' это бот-конфигуратор OmenBoyzCustom /n'
#                                                                        'Я помогу тебе сделать именно тот дизайн, который ты хочешь! Жми "Начать"
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
