import config
import telebot

bot=telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"]) #Старт бота
def command_handler(message):
    markdown = """
        *bold text*
        _italic text_
        [text](URL)
        """
    ret_msg = telebot.send_message(CHAT_ID, markdown, parse_mode="Markdown")
    assert ret_msg.message_id
    
    if message.text == 'Привет' or '/start':
        keyboard_start = telebot.types.InlineKeyboardMarkup()
        callback_button = telebot.types.InlineKeyboardButton(text="Начать", callback_data="test")
        keyboard_start.add(callback_button)
        bot.send_message(message.chat.id, "Привет, " + str(message.chat.first_name) + ", это бот-конфигуратор *OmenBoyzCustom* \n"
                                          "Я помогу тебе сделать именно тот дизайн, который ты хочешь!\n "
                                          "Жми *Начать*", parse_mode="Markdown")
    elif message.text == 'Помощь' or '/help':
        bot.send_message(message.chat.id, "Чем *тебе* помочь?", parse_mode="Markdown")

def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
