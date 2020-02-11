import telebot


bot = telebot.TeleBot('958972895:AAGiG3hlk9Ys1NNGS17dNTeZyETuIDUTzQc')

bus = (["9","46","50","53","60","73",'33'])
bus_code = [
    ["11072","11441","11568","11101","11095","11063"],   #9 
    ["13018","13153","13145","13126","13143","13142","13156","13038"],   #46
    ["13072", "13079", "13038","13059","13066","13113","13161","13073","13148","13078","13108","13112"],  #50
    ["16014","16015","16017","16004","16010","16005","16351","16000"],     #53
    ["11070", "11012",  "11219", "11071","11013","11028","11266","11009"],  # 60
    ["11464","11496", "11408", "11396","11376","11372","11259"],  #73
    ["11136"]    #33
     ]
bus_num = (
     ["447BF01","097YL01","042BM01","275BT01","982AS01","850AS01"],   #9
     ["141AT01","667AX01","650AX01","569AT01","648AX01","647AX01","673AX01","156AT01"],   #46
     ["780AL01", "Z954CA","Z435CA","Z540CA","Z684AU","Z922DA","723CA01","Z859CC","654AX01","Z952CA","Z916DA","921DA01"], #50
     ["839BM01","765BM01","224BZ01","829BM01","834BM01","836BM01","112HC01","759BM01"],    #53
     ["887AS01", "031AT01",  "048BA01", "896AS01","012AT01","102BO01","586BA01","271AT01"],    #60
     ["272BO01","278BO01", "687BM01","587BM01","140BL01","855BL01","026AZ01"],  #73
     ["308BO01"]    #33
)
n1 = len(bus_code[0])
n2 = len(bus_code[1])
n3 = len(bus_code[2])
n4 = len(bus_code[3])
n5 = len(bus_code[4])
n6 = len(bus_code[5])
n7 = len(bus_code[6])
x = (n1+n2+n3+n4+n5+n6+n7)

@bot.message_handler(commands=['start'])
def start_message(message):
         bot.send_message(message.chat.id, 'Отказ от ответственности: Здраствуйте, вы используете данную программу исключительно на свой страх и риск.')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row("Сколько автобусов в базе")
keyboard1.row(f"{bus[0]}",f"{bus[1]}",f"{bus[2]}")
keyboard1.row(f"{bus[3]}",f"{bus[4]}",f"{bus[5]}",f'{bus[6]}' )

@bot.message_handler(commands=['list'])
def start_message(message):
         bot.send_message(message.chat.id, 'Which bus you need' , reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
     if message.text.lower()== f"{bus[0]}":  #9 
          bot.send_message(message.chat.id, f'{message.from_user.first_name}\nАвтобусы которые в имеются базе\n\nБортовой ном:{bus_code[0][0]}\nГосном:{bus_num[0][0]}\n\nБортовой ном:{bus_code[0][1]}\nГосном:{bus_num[0][1]}\n\nБортовой ном:{bus_code[0][2]}\nГосном:{bus_num[0][2]}\n\nБортовой ном:{bus_code[0][3]}\nГосном:{bus_num[0][3]}\n\nБортовой ном:{bus_code[0][4]}\nГосном:{bus_num[0][4]}\n\nБортовой ном:{bus_code[0][5]}\nГосном:{bus_num[0][5]}')
     elif message.text.lower()== f"{bus[1]}":     #46
          bot.send_message(message.chat.id, f'{message.from_user.first_name}\nАвтобусы которые в имеются базе\n\nБортовой ном:{bus_code[1][0]}\nГосном:{bus_num[1][0]}\n\nБортовой ном:{bus_code[1][1]}\nГосном:{bus_num[1][1]}\n\nБортовой ном:{bus_code[1][2]}\nГосном:{bus_num[1][2]}\n\nБортовой ном:{bus_code[1][3]}\nГосном:{bus_num[1][3]}\n\nБортовой ном:{bus_code[1][4]}\nГосном:{bus_num[1][4]}\n\nБортовой ном:{bus_code[1][5]}\nГосном:{bus_num[1][5]}\n\nБортовой ном:{bus_code[1][6]}\nГосном:{bus_num[1][6]}\n\nБортовой ном:{bus_code[1][7]}\nГосном:{bus_num[1][7]}')
     elif message.text.lower()== f"{bus[2]}":     #50
          bot.send_message(message.chat.id, f'{message.from_user.first_name}\nАвтобусы которые в имеются базе\n\nБортовой ном:{bus_code[2][0]}\nГосном:{bus_num[2][0]}\n\nБортовой ном:{bus_code[2][1]}\nГосном:{bus_num[2][1]}\n\nБортовой ном:{bus_code[2][2]}\nГосном:{bus_num[2][2]}\n\nБортовой ном:{bus_code[2][3]}\nГосном:{bus_num[2][3]}\n\nБортовой ном:{bus_code[2][4]}\nГосном:{bus_num[2][4]}\n\nБортовой ном:{bus_code[2][5]}\nГосном:{bus_num[2][5]}\n\nБортовой ном:{bus_code[2][6]}\nГосном:{bus_num[2][6]}\n\nБортовой ном:{bus_code[2][7]}\nГосном:{bus_num[2][7]}\n\nБортовой ном:{bus_code[2][8]}\nГосном:{bus_num[2][8]}\n\nБортовой ном:{bus_code[2][9]}\nГосном:{bus_num[2][9]}\n\nБортовой ном:{bus_code[2][10]}\nГосном:{bus_num[2][10]}\n\nБортовой ном:{bus_code[2][11]}\nГосном:{bus_num[2][11]}')
     elif message.text.lower()== f"{bus[3]}":     #53
          bot.send_message(message.chat.id, f'{message.from_user.first_name}\nАвтобусы которые в имеются базе\n\nБортовой ном:{bus_code[3][0]}\nГосном:{bus_num[3][0]}\n\nБортовой ном:{bus_code[3][1]}\nГосном:{bus_num[3][1]}\n\nБортовой ном:{bus_code[3][2]}\nГосном:{bus_num[3][2]}\n\nБортовой ном:{bus_code[3][3]}\nГосном:{bus_num[3][3]}\n\nБортовой ном:{bus_code[3][4]}\nГосном:{bus_num[3][4]}\n\nБортовой ном:{bus_code[3][5]}\nГосном:{bus_num[3][5]}\n\nБортовой ном:{bus_code[3][6]}\nГосном:{bus_num[3][6]}\n\nБортовой ном:{bus_code[3][7]}\nГосном:{bus_num[3][7]}')
     elif message.text.lower()== f"{bus[4]}":     #60 
          bot.send_message(message.chat.id, f'{message.from_user.first_name}\nАвтобусы которые в имеются базе\n\nБортовой ном:{bus_code[4][0]}\nГосном:{bus_num[4][0]}\n\nБортовой ном:{bus_code[4][1]}\nГосном:{bus_num[4][1]}\n\nБортовой ном:{bus_code[4][2]}\nГосном:{bus_num[4][2]}\n\nБортовой ном:{bus_code[4][3]}\nГосном:{bus_num[4][3]}\n\nБортовой ном:{bus_code[4][4]}\nГосном:{bus_num[4][4]}\n\nБортовой ном:{bus_code[4][5]}\nГосном:{bus_num[4][5]}\n\nБортовой ном:{bus_code[4][6]}\nГосном:{bus_num[4][6]}\n\nБортовой ном:{bus_code[4][7]}\nГосном:{bus_num[4][7]}')
     elif message.text.lower()== f"{bus[5]}":     #73
          bot.send_message(message.chat.id, f'{message.from_user.first_name}\nАвтобусы которые в имеются базе\n\nБортовой ном:{bus_code[5][0]}\nГосном:{bus_num[5][0]}\n\nБортовой ном:{bus_code[5][1]}\nГосном:{bus_num[5][1]}\n\nБортовой ном:{bus_code[5][2]}\nГосном:{bus_num[5][2]}\n\nБортовой ном:{bus_code[5][3]}\nГосном:{bus_num[5][3]}\n\nБортовой ном:{bus_code[5][4]}\nГосном:{bus_num[5][4]}\n\nБортовой ном:{bus_code[5][5]}\nГосном:{bus_num[5][5]}\n\nБортовой ном:{bus_code[5][6]}\nГосном:{bus_num[5][6]}')
     elif message.text.lower()== f"{bus[6]}":     #33
          bot.send_message(message.chat.id, f'{message.from_user.first_name}\nАвтобусы которые в имеются базе\n\nБортовой ном:{bus_code[6][0]}\nГосном:{bus_num[6][0]}')
     elif message.text == "Сколько автобусов в базе":
          bot.send_message(message.chat.id, f'Общее количество {x}' )

if __name__ == '__main__':
     bot.infinity_polling()