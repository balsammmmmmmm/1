import telebot
bot = telebot.TeleBot('1023490470:AAH7uNsJex1ClxKuiMCDRfrjD-5I7I84fCA')


keyboard1 = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard1.row("добавить инфо")
qq = []

@bot.message_handler(commands=['start'])
def start_message(message):
         bot.send_message(message.chat.id, 'Which day you need' , reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
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
    qq.append(message.text)
    bot.send_message(message.chat.id, qq[0])
    #Здесь мы сохраняем значение message.text в наш массив qq
    #И бот отправляет нам первый элемент списка qq(для наглядности, что message.text добавлен




if __name__ == '__main__':
    bot.infinity_polling()