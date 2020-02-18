import telebot
from datetime import datetime
bot = telebot.TeleBot('1022871098:AAH-gj6y-0lunQYgj0WSiGgJmyVl5btR5XY')


keyboard1 = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard1.row("добавить инфо")

@bot.message_handler(content_types=['text'])
def start_message(message):
        bot.send_message(message.chat.id, 'Which day you need' , reply_markup=keyboard1)
        if message.text == 'добавить инфо':
            bot.register_next_step_handler(message, infoAdding)
#если message.text == добавить инфо - мы переходим к функции infoAdding, message - #обязательный параметр, в нем храниться вся информация о сообщении
#(имя пользователя который его прислал, текст сообщения, id и тд..)
def infoAdding(message):
    msg=bot.send_message(message.chat.id, "Введите информацию")
    bot.register_next_step_handler(msg, result)
    #Здесь, в  infoAdding - пользователь вводит нужную информацию,  
    #чтобы её получить нам нужно перейти к другой в функции
    # в нашем случае result но может быть любая другая. 
    # Тогда в функции result придет сообщение(message) с текстом который ввёл пользователь
def result(message):
    curTime = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_surname = message.from_user.last_name
    file_object = open('users.txt', 'a' )
    file_object.write(message.text+" "+str(user_id) + " " + user_name + " " + user_surname + " " + curTime + "\n")
    file_object.close()
    bot.send_message(message.chat.id, "done")
    #Здесь мы сохраняем значение message.text в наш массив qq
    #И бот отправляет нам первый элемент списка qq(для наглядности, что message.text добавлен


if __name__ == '__main__':
    bot.infinity_polling()