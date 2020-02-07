import telebot


bot = telebot.TeleBot('958972895:AAGiG3hlk9Ys1NNGS17dNTeZyETuIDUTzQc')

bus = (["9","46","50","53","60","73",'33'])
bus_code = [
    ["11072","11441"],   #9 
    ["018"],   #46
    ["13072", "13079", "13038","13059","13066"],  #50
    ["0"],     #53
    ["11070", "11012",  "11219", "11071","11013","11028"],  # 60
    ["11464","11496", "11408", "11396","11376"],  #73
    ["136"]    #33
     ]
bus_num = (
     ["447BF01","097YL01"],   #9
     ["141AT01"],   #46
     ["780AL01", "Z954CA","Z435CA","Z540CA","Z684AU"], #50
     ["0"],    #53
     ["887AS01", "031AT01",  "048BA01", "896AS01","012AT01","102BO01"],    #60
     ["272BO01","278BO01", "687BM01","587BM01","140BL01"],  #73
     ["308BO01"]    #33
)


@bot.message_handler(commands=['start'])
def start_message(message):
         bot.send_message(message.chat.id, 'Отказ от ответственности: Здраствуйте, вы используете данную программу исключительно на свой страх и риск.')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row(f"{bus[0]}",f"{bus[1]}",f"{bus[2]}")
keyboard1.row(f"{bus[3]}",f"{bus[4]}",f"{bus[5]}",f'{bus[6]}' )

@bot.message_handler(commands=['list'])
def start_message(message):
         bot.send_message(message.chat.id, 'Which bus you need' , reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
     if message.text.lower()== f"{bus[0]}":
          bot.send_message(message.chat.id, f'{message.from_user.first_name}\nАвтобусы которые в имеются базе\n\nБортовой ном:{bus_code[0][0]}\nГосном:{bus_num[0][0]}\n\nБортовой ном:{bus_code[0][1]}\nГосном:{bus_num[0][1]}')
     elif message.text.lower()== f"{bus[1]}":
          bot.send_message(message.chat.id, f'{message.from_user.first_name}\nАвтобусы которые в имеются базе\n\nБортовой ном:{bus_code[1][0]}\nГосном:{bus_num[1][0]}')
     elif message.text.lower()== f"{bus[2]}":
          bot.send_message(message.chat.id, f'{message.from_user.first_name}\nАвтобусы которые в имеются базе\n\nБортовой ном:{bus_code[2][0]}\nГосном:{bus_num[2][0]}\n\nБортовой ном:{bus_code[2][1]}\nГосном:{bus_num[2][1]}\n\nБортовой ном:{bus_code[2][2]}\nГосном:{bus_num[2][2]}\n\nБортовой ном:{bus_code[2][3]}\nГосном:{bus_num[2][3]}\n\nБортовой ном:{bus_code[2][4]}\nГосном:{bus_num[2][4]}')
     elif message.text.lower()== f"{bus[3]}":
          bot.send_message(message.chat.id, f'{message.from_user.first_name}\nАвтобусы которые в имеются базе\n\nБортовой ном:{bus_code[3][0]}\nГосном:{bus_num[3][0]}')
     elif message.text.lower()== f"{bus[4]}":
          bot.send_message(message.chat.id, f'{message.from_user.first_name}\nАвтобусы которые в имеются базе\n\nБортовой ном:{bus_code[4][0]}\nГосном:{bus_num[4][0]}\n\nБортовой ном:{bus_code[4][1]}\nГосном:{bus_num[4][1]}\n\nБортовой ном:{bus_code[4][2]}\nГосном:{bus_num[4][2]}\n\nБортовой ном:{bus_code[4][3]}\nГосном:{bus_num[4][3]}\n\nБортовой ном:{bus_code[4][4]}\nГосном:{bus_num[4][4]}\n\nБортовой ном:{bus_code[4][5]}\nГосном:{bus_num[4][5]}')
     elif message.text.lower()== f"{bus[5]}":
          bot.send_message(message.chat.id, f'{message.from_user.first_name}\nАвтобусы которые в имеются базе\n\nБортовой ном:{bus_code[5][0]}\nГосном:{bus_num[5][0]}\n\nБортовой ном:{bus_code[5][1]}\nГосном:{bus_num[5][1]}\n\nБортовой ном:{bus_code[5][2]}\nГосном:{bus_num[5][2]}\n\nБортовой ном:{bus_code[5][3]}\nГосном:{bus_num[5][3]}\n\nБортовой ном:{bus_code[5][4]}\nГосном:{bus_num[5][4]}')
     elif message.text.lower()== f"{bus[6]}":
          bot.send_message(message.chat.id, f'{message.from_user.first_name}\nАвтобусы которые в имеются базе\n\nБортовой ном:{bus_code[6][0]}\nГосном:{bus_num[6][0]}')


if __name__ == '__main__':
     bot.infinity_polling()