import telebot


bot = telebot.TeleBot('1023490470:AAH7uNsJex1ClxKuiMCDRfrjD-5I7I84fCA')

day = (["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота"])
day_0 = (
     ["10:00 - 10:50\nИностранный язык,'прак' (преподаватель-магистр Сулейменова Ж.А.), К02. Учебный корпус №2, ФИТ, 216\n\n11:00 - 11:50\nМатематика 2,'лек' (и.о.доцента Оспанов М.Н.), К02. Учебный корпус №2, ФИТ, 222\n\n12:10 - 13:00\nАлгоритмы, структуры данных и программирование,'лек' (и.о. доцента Айтқожа Ж.Ж.), К02. Учебный корпус №2, ФИТ, 221",
     "Пар нет, отдыхаем"]
)
day_1 = (
     ['Пар нет, отдыхаем',
     "12:10 - 13:00\nОперациялық жүйелер қауіпсіздігі,'лек' (преподаватель Каманур Ү.), К02. Учебный корпус №2, ФИТ, 221\n\n13:10 - 14:00\nОперациялық жүйелер қауіпсіздігі,'лек' (преподаватель Каманур Ү.), К02. Учебный корпус №2, ФИТ, 221\n\n14:10 - 15:00\n Окно\n15:10 - 16:00\n Окно\n16:10 - 17:00\nДене шынықтыру,'прак' (Старший преподаватель Сидорова Р.В.)\n\n17:10 - 18:00\nДене шынықтыру,'прак' (Старший преподаватель Сидорова Р.В.)"]
)
day_2 = (
     ["8:00 - 8:50\nАлгоритмы, структуры данных и программирование,'лаб' ( Адалбек А.), К02. Учебный корпус №2, ФИТ, 608\n\n9:00 - 9:50\nАлгоритмы, структуры данных и программирование,'лаб' ( Адалбек А.), К02. Учебный корпус №2, ФИТ, 608\n\n10:00 - 10:50\nКазахский (русский) язык 2,'прак' ( Шахин А.А.), К02. Учебный корпус №2, ФИТ, 711",
     "14:10 - 15:00\nКриптография,'лек' ( Конырханова А.А.), К02. Учебный корпус №2, ФИТ, 221\n\n15:10 - 16:00\nКриптография,'лек' ( Конырханова А.А.), К02. Учебный корпус №2, ФИТ, 221\n\n16:10 - 17:00\nКриптография,'прак' ( Мукушева Н.Ж.), К02. Учебный корпус №2, ФИТ, 302"]
)

day_3 = (
     ["10:00 - 10:50\nФизическая культура,'прак' (и.о. профессора Омаров Е.Б.)\n\n11:00 - 11:50\nФизическая культура,'прак' (и.о. профессора Омаров Е.Б.)\n\n12:10 - 13:00\nКазахский (русский) язык 2,'прак' ( Шахин А.А.), К02. Учебный корпус №2, ФИТ, 711\n\n13:10 - 14:00\nКазахский (русский) язык 2,'прак' ( Шахин А.А.), К02. Учебный корпус №2, ФИТ, 711",
     "12:10 - 13:00\nФилософия,'лек' ( Кенжеев А.А.), К02. Учебный корпус №2, ФИТ, 221\n\n13:10 - 14:00\nФилософия,'лек' ( Кенжеев А.А.), К02. Учебный корпус №2, ФИТ, 221\n\n14:10 - 15:00\nКәсіби қазақ (орыс) тілі*,'прак' (ст. преп. Яворская Э.Э.), К02. Учебный корпус №2, ФИТ, 302\n\n15:10 - 16:00\nКәсіби қазақ (орыс) тілі*,'прак' (ст. преп. Яворская Э.Э.), К02. Учебный корпус №2, ФИТ, 302\n\n16:10 - 17:00\nЦифрлық сұлбатехника,'прак' ( Мукушева Н.Ж.), К02. Учебный корпус №2, ФИТ, 508a\n\n17:10 - 18:00\nЦифрлық сұлбатехника,'прак' ( Мукушева Н.Ж.), К02. Учебный корпус №2, ФИТ, 508a"]
)

day_4 = (
     ["8:00 - 8:50\nИнформационно-коммуникационные технологии,'лек' (ст.преподаватель Оспанов Р.М.), К02. Учебный корпус №2, ФИТ, 712\n\n9:00 - 9:50\nИнформационно-коммуникационные технологии,'лек' (ст.преподаватель Оспанов Р.М.), К02. Учебный корпус №2, ФИТ, 712\n\n10:00 - 10:50\n Окно\n\n11:00 - 11:50\nИнформационно-коммуникационные технологии,'прак' ( Хамитова Ж.Ж.), К01. Учебный корпус №1, УАК, 352a",
     "14:10 - 15:00\nЦифрлық сұлбатехника,'лек' (PhD доктор, ст. преподаватель Бурибаева А.К.), К02. Учебный корпус №2, ФИТ, 221\n\n15:10 - 16:00\nКриптографияның математикалық негіздері,'лек' (к.ф.-м.н., доцент Сексенбаева А.К.), К02. Учебный корпус №2, ФИТ, 221\n\n16:10 - 17:00\nКриптографияның математикалық негіздері,'лек' (к.ф.-м.н., доцент Сексенбаева А.К.), К02. Учебный корпус №2, ФИТ, 221\n\n17:10 - 18:00\nОперациялық жүйелер қауіпсіздігі,'прак' ( Мукушева Н.Ж.), К02. Учебный корпус №2, ФИТ, 414"]
)

day_5 = (
     ["10:00 - 10:50\nМатематика 2,'прак' (ст.преп. Ахажанов Т.Б.), К02. Учебный корпус №2, ФИТ, 707\n\n11:00 - 11:50\nМатематика 2,'прак' (ст.преп. Ахажанов Т.Б.), К02. Учебный корпус №2, ФИТ, 707\n\n12:10 - 13:00\nИностранный язык,'прак' (преподаватель-магистр Сулейменова Ж.А.), К02. Учебный корпус №2, ФИТ, 707\n\n13:10 - 14:00\nИностранный язык,'прак' (преподаватель-магистр Сулейменова Ж.А.), К02. Учебный корпус №2, ФИТ, 707",
     "10:00 - 10:50\nФилософия,'прак' (преподаватель Уралбаева Ш.К.), К04. Учебный корпус №4, ПЕД , 220\n\n11:00 - 11:50\nКриптографияның математикалық негіздері,'прак' (к.ф.-м.н., доцент Сексенбаева А.К.), К02. Учебный корпус №2, ФИТ, 224"]
)
uni_gr = (["АЖ-19/1","СИБ-23"])

keyboard1 = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard1.row(f"{uni_gr[0]}",f"{uni_gr[1]}")

keyboard2 = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard2.row(f"{day[0]}",f"{day[1]}",f"{day[2]}")
keyboard2.row(f"{day[3]}",f"{day[4]}",f"{day[5]}")

@bot.message_handler(commands=['start'])
def start_message(message):
     bot.send_message(message.chat.id, 'Which group you need' , reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
     if message.text == f"{uni_gr[0]}":
          msg = bot.send_message(message.chat.id, 'Which day you need' , reply_markup=keyboard2)
          bot.register_next_step_handler(msg, send_shedudle)
     elif message.text == f"{uni_gr[1]}":
          msg = bot.send_message(message.chat.id, 'Which day you need' , reply_markup=keyboard2)
          bot.register_next_step_handler(msg, send_shedudle2)

def send_shedudle(message):
     if message.text == f"{day[0]}":
          bot.send_message(message.chat.id, f'Здраствуйте {message.from_user.first_name}\nСегодня:\n\n{day_0[0]}',reply_markup=keyboard1)
     elif message.text == f"{day[1]}":
          bot.send_message(message.chat.id, f'Здраствуйте {message.from_user.first_name}\nСегодня:\n\n{day_1[0]}',reply_markup=keyboard1)
     elif message.text == f"{day[2]}":
          bot.send_message(message.chat.id, f'Здраствуйте {message.from_user.first_name}\nСегодня:\n\n{day_2[0]}',reply_markup=keyboard1)
     elif message.text == f"{day[3]}":
          bot.send_message(message.chat.id, f'Здраствуйте {message.from_user.first_name}\nСегодня:\n\n{day_3[0]}',reply_markup=keyboard1)
     elif message.text == f"{day[4]}":
          bot.send_message(message.chat.id, f'Здраствуйте {message.from_user.first_name}\nСегодня:\n\n{day_4[0]}',reply_markup=keyboard1)
     elif message.text == f"{day[5]}":
          bot.send_message(message.chat.id, f'Здраствуйте {message.from_user.first_name}\nСегодня:\n\n{day_5[0]}',reply_markup=keyboard1)

def send_shedudle2(message):
          if message.text == f"{day[0]}":
               bot.send_message(message.chat.id, f'Здраствуйте {message.from_user.first_name}\nСегодня:\n\n{day_0[1]}',reply_markup=keyboard1)
          elif message.text == f"{day[1]}":
               bot.send_message(message.chat.id, f'Здраствуйте {message.from_user.first_name}\nСегодня:\n\n{day_1[1]}',reply_markup=keyboard1)
          elif message.text == f"{day[2]}":
               bot.send_message(message.chat.id, f'Здраствуйте {message.from_user.first_name}\nСегодня:\n\n{day_2[1]}',reply_markup=keyboard1)
          elif message.text == f"{day[3]}":
               bot.send_message(message.chat.id, f'Здраствуйте {message.from_user.first_name}\nСегодня:\n\n{day_3[1]}',reply_markup=keyboard1)
          elif message.text == f"{day[4]}":
               bot.send_message(message.chat.id, f'Здраствуйте {message.from_user.first_name}\nСегодня:\n\n{day_4[1]}',reply_markup=keyboard1)
          elif message.text == f"{day[5]}":
               bot.send_message(message.chat.id, f'Здраствуйте {message.from_user.first_name}\nСегодня:\n\n{day_5[1]}',reply_markup=keyboard1)
          
if __name__ == '__main__':
     bot.infinity_polling()