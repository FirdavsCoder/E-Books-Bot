#  _____  _            _                     _            _
# |  ___|(_) _ __   __| |  __ _ __   __ ___ | |__    ___ | | __
# | |_   | || '__| / _` | / _` |\ \ / // __|| '_ \  / _ \| |/ /
# |  _|  | || |   | (_| || (_| | \ V / \__ \| |_) ||  __/|   <
# |_|    |_||_|    \__,_| \__,_|  \_/  |___/|_.__/  \___||_|\_\


#  ____
# |  _ \  _ __   ___    __ _  _ __   __ _  _ __ ___   _ __ ___    ___  _ __
# | |_) || '__| / _ \  / _` || '__| / _` || '_ ` _ \ | '_ ` _ \  / _ \| '__|
# |  __/ | |   | (_) || (_| || |   | (_| || | | | | || | | | | ||  __/| |
# |_|    |_|    \___/  \__, ||_|    \__,_||_| |_| |_||_| |_| |_| \___||_|
#                      |___/




import logging
from xml.dom.minidom import Document
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import sqlite3
import datetime
import pytz

print("Bot started...")


TOKEN = "5782664696:AAG447bozRMO9B_qkjbu0HAOsYY2I6DvIcs"




logging.basicConfig(level = logging.INFO)

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)








@dp.message_handler(commands = ['start'])
async def command_start(message: types.Message):
    connect = sqlite3.connect('./data.db')
    cursor = connect.cursor()
    cursor.execute(
            """CREATE TABLE IF NOT EXISTS users ("key"  INTEGER,"user_id"  INTEGER,"date"  INTEGER);""")
    if cursor.execute(f"""SELECT user_id FROM users WHERE user_id = {message.chat.id}""").fetchone() == None:
            sana = datetime.datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%d-%m-%Y %H:%M')
            cursor.execute(
                "INSERT INTO users (user_id, date) VALUES ('{user_id}', '{sana}')".format(user_id=message.chat.id,
                                                                                          sana=sana))
            connect.commit()
    await bot.send_message(message.from_user.id, "Salom {0.first_name}\nFirdavsbek Yorkulovning Elektron darsliklar botiga xush kelibsiz!\nAyrim darsliklar topilmagani sababli bot bazadagi boshqa kitoblarni chiqarib yuborishi mumkin.\nBuning uchun uzr soraymiz\nMarhamat Botdan yaxshi maqsadda foydalaning".format(message.from_user), reply_markup= nav.mainMenu)
    await bot.send_message(message.from_user.id, "Botdan foydalanish uchun tezkor komandalar:\n/admin - admin kim\n/help - yordam uchun\n/1 - Otkan kunlar\n/2 - Jinlar bazmi\n/3 - Quyonlar saltanati\n/4 - Sariq devning olimi\nAudio Kitoblar:\n/5 - Shum bola audiosi\n/6 - Me'mor audio hikoya\n/7 - Garov\n/8 - Taras Bulba\n/9 - Shamol yolidagi qabriston\n/10 - Kitob savdosi\n/11 - Yutuq\n/12 - Qurigan daraxt\n/booknomy - Booknomy ingliz tili uchun\n/epub - EPUB o'quvchi dastur\n/avtotest - AvtoTest uchun\n/TedBook - TedBook elektron kitobi\n/followers - botdagi obunachilar sonini bilish\n\n\nProgrammer: Firdavsbek Yorkulov @Firdavs_Programmer")



@dp.message_handler(text =  "followers")
async def statistics(message: types.Message):
    connect = sqlite3.connect('./data.db')
    cursor = connect.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    followers = cursor.fetchone()[0]
  

    await message.answer(f"📊 Statistika\n"
                         f"🫂 Botdagi jami foydalanuvchilar soni:  {followers}\n")
                         
                         
@dp.message_handler(commands = ['followers'])
async def statistics(message: types.Message):
    connect = sqlite3.connect('./data.db')
    cursor = connect.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    followers = cursor.fetchone()[0]
  

    await message.answer(f"📊 Statistika\n"
                         f"🫂 Botdagi jami foydalanuvchilar soni:  {followers}\n")
                         



@dp.message_handler(commands = ['avtotest'])
async def command_avtotest(message: types.Message):
	await message.reply_document(document = "https://t.me/apklar_kitob_baza/72")

@dp.message_handler(commands=['TedBook'])
async def command_tedbook(message: types.Message):
    await message.reply_document(document="tedbook's link here")


@dp.message_handler(commands = ['epub'])
async def command_epub(message: types.Message):
	await message.reply_document(document = "https://t.me/apklar_kitob_baza/62")


@dp.message_handler(commands = ['booknomy'])
async def command_13(message: types.Message):
	await message.reply_document(document = "https://t.me/booknomy_baza/4")
	await message.reply_document(document = "https://t.me/booknomy_baza/6")
	await message.reply_document(document = "https://t.me/booknomy_baza/3")
	await message.reply_document(document = "https://t.me/booknomy_baza/2")
	await message.reply_document(document = "https://t.me/booknomy_baza/5")
	await message.reply_document(document = "https://t.me/booknomy_baza/7")
	await message.reply_document(document = "https://t.me/booknomy_baza/8")
	await message.reply_document(document = "https://t.me/booknomy_baza/9")




@dp.message_handler(commands = ['12'])
async def command_12(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/388")





@dp.message_handler(commands = ['11'])
async def command_11(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/386")



@dp.message_handler(commands = ['10'])
async def command_10(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/385")



@dp.message_handler(commands = ['9'])
async def command_9(message: types.Message):
    await message.reply_document(document  ="https://t.me/firdavsbek1551/387")


@dp.message_handler(commands = ['8'])
async def command_8(message: types.Message):
    await message.reply_document(document ="https://t.me/firdavsbek1551/383")







@dp.message_handler(commands = ['7'])
async def command_7(message: types.Message):
    await message.reply_document(document ="https://t.me/firdavsbek1551/381")



@dp.message_handler(commands  =['6'])
async def command_6(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/384")


@dp.message_handler(commands = ['5'])
async def command_5(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/380")


@dp.message_handler(commands = ['admin'])
async def command_admin(message: types.Message):
    await bot.send_message(message.chat.id, "Assalomu alaykum!\nHurmatli foydalanuvchi botimiz admini: Firdavsbek Yorkulov.\nAdmin bilan aloqa:\nTelegram: @Firdavs_Programmer\nWeb-site: firdavsbek07.netlify.app\nBotimizdan foydalanayotganingiz uchun, rahmat.")

@dp.message_handler(commands = ['audio'])
async def command_audio(message: types.Message):
    await bot.send_message(message.from_user.id, "Assalomu alaykum!".format(message.from_user), reply_markup= nav.menuAudioBooks)

@dp.message_handler(commands = ['4'])
async def command_4(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/243")



@dp.message_handler(commands = ['3'])
async def command_3(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/241")




@dp.message_handler(commands = ['2'])
async def command_2(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/244")



@dp.message_handler(commands = ['1'])
async def command_1(message: types.Message):
    await message.reply_document(document = "https://t.me/firdavsbek1551/247")



@dp.message_handler(commands = ['help'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, "Botdan foydalanish uchun\n/start buyrug'ini bering. Va pastdan chiqgan tugmalardan mosini tanlang.\nCreator: Firdavs Yorkulov\nMurojaat uchun:\nTelegram: @Firdavs_Programmer\nWeb-site: firdavsbek07.netlify.app.")

















@dp.message_handler()
async def bot_message(message: types.Message):
    #await bot.send_message(message.from_user.id, message.text)
    if message.text=="📘Maktab darsliklari📘":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuSinflar)

    elif message.text =="TedBook kitobi":
        await message.reply_document(document = "https://t.me/link_kanal_baza/33", caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Ruscha kitoblar":
        await message.reply_document(document= "https://t.me/link_kanal_baza/42", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/link_kanal_baza/46", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/link_kanal_baza/43", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/link_kanal_baza/44", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/link_kanal_baza/45", caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Murphy books":
        await message.reply_document(document= "https://t.me/link_kanal_baza/36", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/link_kanal_baza/40", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/link_kanal_baza/38", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/link_kanal_baza/39", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/link_kanal_baza/37", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/link_kanal_baza/58", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/link_kanal_baza/60", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/link_kanal_baza/59", caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Test master":
        await message.reply_document(document= "https://t.me/link_kanal_baza/55", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/link_kanal_baza/57", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/link_kanal_baza/56", caption="Dasturchi @Firdavs_Programmer")

    elif message.text =="Other books":
        await message.reply_document(document= "https://t.me/c/1768848912/36", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/34", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/37", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/32", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/35", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/33", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/38", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/40", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/42", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/41", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/39", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/43", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/44", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/47", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/49", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/48", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/46", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/45", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/52", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/50", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document= "https://t.me/c/1768848912/51", caption="Dasturchi @Firdavs_Programmer")
    

    elif message.text =="JavaScript":
        await message.reply_document(document="https://t.me/link_kanal_baza/101", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/106", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/100", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/105", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/107", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/108", caption="Dasturchi @Firdavs_Programmer")

    elif message.text =="English books":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuenbooks)

    elif message.text =="Php":
        await message.reply_document(document="https://t.me/link_kanal_baza/113", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/111", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/112", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/116", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/117", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/114", caption="Dasturchi @Firdavs_Programmer")

    
    elif message.text =="Python":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menupythonbooks)

    elif message.text =="Java":
        await message.reply_document(document="https://t.me/link_kanal_baza/98", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/102", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/108", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/103", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/99", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/104", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/98", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/102", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/103", caption="Dasturchi @Firdavs_Programmer")


    elif message.text =="Django kitoblar":
        await message.reply_document(document="https://t.me/link_kanal_baza/83", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/85", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/84", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/86", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/90", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/87", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/88", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/91", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/89", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/93", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/92", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/94", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/95", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/96", caption="Dasturchi @Firdavs_Programmer")


    elif message.text =="O'quv qo'llanmalri":
        await message.reply_document(document="https://t.me/link_kanal_baza/65", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/63", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/62", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/64", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/67", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/70", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/71", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/69", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/66", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/68", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/73", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/75", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/72", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/76", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/74", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/80", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/77", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/81", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/78", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/79", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="", caption="Dasturchi @Firdavs_Programmer")


    elif message.text =="HTML":
        await message.reply_document(document="https://t.me/link_kanal_baza/121", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/124", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/123", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/120", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/122", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/125", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/126", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="", caption="Dasturchi @Firdavs_Programmer")

    elif message.text =="CSS":
        await message.reply_document(document="https://t.me/link_kanal_baza/128", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/132", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/133", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/131", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/130", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/129", caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document="https://t.me/link_kanal_baza/134", caption="Dasturchi @Firdavs_Programmer")


    elif message.text =="Dasturlash kitoblari":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuebooks)
        
    elif message.text =="🇺🇸Ingliz tili bilimdon🇺🇸":
        await message.reply_document(document ="https://t.me/apklar_kitob_baza/74")
        
    elif message.text =="🇷🇺Rus tili bilimdon🇷🇺":
        await message.reply_document(document ="https://t.me/apklar_kitob_baza/76")
    
    if message.text=="😊 Orqaga":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuSinflar)
    
    if message.text=="💻 Informatika":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuInformatika)
    
    if message.text=="🔙 Back":
        await bot.send_message(message.from_user.id, message.text, reply_markup=vid.menuVideo)

    elif message.text =="🧑‍💻Admin🧑‍💻":
    	await bot.send_message(message.from_user.id, "Bot admini: @Firdavs_Programmer")


    elif message.text == "🚔Avto Test✅":
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/72")


    elif message.text == "🧑‍💻Admin bilan aloqa🧑‍💻":
    	await bot.send_message(message.from_user.id, message.text, reply_markup = nav.btnaloqaMenu)


    elif message.text == "🎧5-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/184",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/181",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/185",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/182",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/183",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖6-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/244",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/249",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/241",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/252",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/250",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/248",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/243",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/245",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/247",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/239",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/255",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/253",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/242",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/240",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/257",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/256",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/246",caption="Dasturchi @Firdavs_Programmer")



    elif message.text == "📖7-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/259",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/263",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/261",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/260",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/264",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/262",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/265",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/266",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/268",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/269",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/267",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/270",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/272",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/271",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/273",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/276",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/274",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/277",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/275",caption="Dasturchi @Firdavs_Programmer")


    elif message.text =="📖8-sinf🎧":
        await message.reply_document(document = "https://t.me/booknomy_baza/83",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/86",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/85",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/84",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/87",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/90",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/91",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/92",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/89",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/88",caption="Dasturchi @Firdavs_Programmer")
        

    elif message.text =="📖9-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/284",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/283",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/285",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/286",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/282",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/281",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/287",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/289",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/290",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/288",caption="Dasturchi @Firdavs_Programmer")
        
    elif message.text == "📖10-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/294",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/299",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/293",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/301",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/297",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/296",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/295",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/292",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/300",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/298",caption="Dasturchi @Firdavs_Programmer")


    elif message.text =="Fizika":
        await message.reply_document(document = "https://t.me/booknomy_baza/20",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/21",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/22",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/23",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/24",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Kimyo Biologiya":
        await message.reply_document(document = "https://t.me/apklar_kitob_baza/79",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/apklar_kitob_baza/80",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/apklar_kitob_baza/83",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/apklar_kitob_baza/82",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/apklar_kitob_baza/85",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/apklar_kitob_baza/81",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/apklar_kitob_baza/84",caption="Dasturchi @Firdavs_Programmer")


    elif message.text == "📖11-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/303",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/308",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/307",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/305",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/312",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/306",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/304",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/310",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/317",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/313",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/315",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/311",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/314",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/316",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/309",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/321",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/319",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/318",caption="Dasturchi @Firdavs_Programmer")
    
    elif message.text =="🎧6-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/188",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/187",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/189",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/190",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/191",caption="Dasturchi @Firdavs_Programmer")
    
    elif message.text == "🎧7-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/194",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/193",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "🎧8-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/198",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/199",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/197",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "🎧9-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/202",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/201",caption="Dasturchi @Firdavs_Programmer")



    elif message.text == "🎧10-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/205",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/206",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/204",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/205",caption="Dasturchi @Firdavs_Programmer")


    elif message.text == "🎧11-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/211",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/212",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/213",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/215",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/217",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/214",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/216",caption="Dasturchi @Firdavs_Programmer")
    elif message.text =="📖5-sinf🎧":
        await message.reply_document(document = "https://t.me/audios_baza/220",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/221",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/222",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/219",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/223",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/224",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/227",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/226",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/228",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/225",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "")


    elif message.text == "🗣Audio ertaklar":
        await message.reply_document(document = "https://t.me/audios_baza/334",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/335",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/338",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/336",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/341",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/339",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/340",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/337",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/342",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/344",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/345",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/346",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/343",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/347",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/351",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "🗣Audio hikoyalar🗣":
        await message.reply_document(document = "https://t.me/audios_baza/356",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/357",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/355",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/358",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/360",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/359",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/363",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/361",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/362",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/366",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/364",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/365",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/368",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/367",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/373",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/374",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/370",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/audios_baza/372",caption="Dasturchi @Firdavs_Programmer")


    elif message.text == "🧑‍💻Web saytimiz🧑‍💻":
    	await bot.send_message(message.from_user.id, "Bizning Web Saytimiz:\nhttps://firdavsbek07.netlify.app")

    elif message.text == "🧑‍💻Instagram🧑‍💻":
    	await bot.send_message(message.from_user.id, "Bizning Instagram sahifamiz:\nhttps://www.instagram.com/firdavs_python_developer")

    elif message.text =="🧑‍💻Telegram🧑‍💻":
    	await bot.send_message(message.from_user.id, "Bizning Telegram sahifamiz:\nhttps://t.me/Firdavs_Programmer")

    elif message.text =="🧑‍💻Facebook🧑‍💻":
    	await bot.send_message(message.from_user.id, "Bizning Facebook sahifamiz: \nhttps://www.facebook.com/profile.php?id=100077125194410")


    elif message.text =="🧑‍💻GitHub🧑‍💻":
    	await bot.send_message(message.from_user.id, "Bizning GitHub sahifamiz: \nhttps://github.com/firdavsbekyorkulov")


    elif message.text =="📲Kitoblarni o'quvchi dastur📲":
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/64",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/65",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/66",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/67",caption="Dasturchi @Firdavs_Programmer")



    elif message.text == "📖Rus tili✅":
    	await message.reply_document(document ="https://t.me/booknomy_baza/12",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document ="https://t.me/booknomy_baza/11",caption="Dasturchi @Firdavs_Programmer")


    elif message.text =="📖Koreys tili✅":
    	await message.reply_document(document = "https://t.me/booknomy_baza/15",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/booknomy_baza/14",caption="Dasturchi @Firdavs_Programmer")



    elif message.text =="📖Ona tili audio📖":
    	await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuOnatili)

    elif message.text =="🖋Adabiyot audio🖋":
    	await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuAdabuyotAudio)

    elif message.text =="🕰Tarix audio":
    	await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuTarixAudio)

    elif message.text =="☘️Biologiya audio☘️":
    	await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuBiology)


    elif message.text == "📖Islom Karimov asarlari📖":
        await message.reply_document(document = "https://t.me/booknomy_baza/66",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/67",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/69",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/68",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/72",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/70",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/73",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/71",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/75",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/74",caption="Dasturchi @Firdavs_Programmer")
        

        
    elif message.text == "📖Shavkat Mirziyoyev asarlari📖":
        await message.reply_document(document = "https://t.me/booknomy_baza/77",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/80",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/79",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/81",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/78",caption="Dasturchi @Firdavs_Programmer")


    elif message.text == "📖Alisher Navoiy asarlari📖":
        await message.reply_document(document = "https://t.me/booknomy_baza/55",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/57",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/56",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/62",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/61",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/58",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/60",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/64",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/63",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/59",caption="Dasturchi @Firdavs_Programmer")



    elif message.text == "📖Sheriyat📖":
        await bot.send_message(message.from_user.id, message.text, reply_markup = nav.btnMenuSheriy)



    elif message.text =="📖Muhammad Yusuf📖":
        await message.reply_document(document = "https://t.me/booknomy_baza/27",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/32",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/33",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/35",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/28",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/34",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/30",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/31",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/29",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/36",caption="Dasturchi @Firdavs_Programmer")


    elif message.text == "📖Erkin Vohidov📖":
        await message.reply_document(document = "https://t.me/booknomy_baza/42",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/39",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/38",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/40",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/41",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/45",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/43",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/47",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/44",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/46",caption="Dasturchi @Firdavs_Programmer")



    elif message.text =="📖Abdulla Oripov📖":
        await message.reply_document(document = "https://t.me/booknomy_baza/50",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/51",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/49",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/53",caption="Dasturchi @Firdavs_Programmer")
        await message.reply_document(document = "https://t.me/booknomy_baza/52",caption="Dasturchi @Firdavs_Programmer")


    elif message.text =="":
        await message.reply_document(document = "")





    elif message.text =="🇺🇿O'zbekiston Milliy Ensiklopediyasi🇺🇿":
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/9",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/10",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/7",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/4",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/15",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/14",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/3",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/5",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/2",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/6",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/8",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/18",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/17",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/13",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/11",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/12",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/19",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/16",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/20",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/24",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/25",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/27",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/28",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/22",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/21",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/29",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/30",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/26",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/ensiklopediyalar_baza/23",caption="Dasturchi @Firdavs_Programmer")
    	
    
    elif message.text=="♻️Botni guruhga qo'shish✅":
    	await bot.send_message(message.from_user.id, "Botni guruhga qo'shish uchun: ushbu linkdan foydalaning:\nhttps:telegram.me/Elektron_kutubxona_uz_robot?startgroup=new \nBotni ulashish uchun esa mana bu linkdan foydalaning: \nhttps://t.me/url?url=https://t.me/Elektron_kutubxona_uz_robot?start \nBotimizdan foydalanganingiz uchun rahmat!")


    elif message.text =="📂EPUBni ochish dasturi✅":
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/62",caption="Dasturchi @Firdavs_Programmer")

    elif message.text =="📖Ingliz tili✅":
    	await message.reply_document(document = "https://t.me/booknomy_baza/4",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/booknomy_baza/6",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/booknomy_baza/3",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/booknomy_baza/2",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/booknomy_baza/5",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/booknomy_baza/7",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/booknomy_baza/8",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/booknomy_baza/9",caption="Dasturchi @Firdavs_Programmer")

    elif message.text =="🇺🇸Booknomy":
    	await bot.send_message(message.from_user.id, message.text, reply_markup = nav.menuBooknomy)

    elif message.text =="🇺🇸Lug'atlar":
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/52",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/53",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/54",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/55",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/56",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/57",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/58",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/59",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/60",caption="Dasturchi @Firdavs_Programmer")
    	



    elif message.text == "📐Matematika":
    	await message.reply_document(document = "https://t.me/firdavsbek1551/466",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/469",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/467",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/468",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/465",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/473",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/471",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/470",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/472",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/474",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/481",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/476",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/477",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/479",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/475",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/478",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/480",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/483",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/482",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/firdavsbek1551/484",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "")





    elif message.text == "📲Apk kitoblar📕":
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/2",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/3",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/4",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/5",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/6",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/7",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/8",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/9",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/10",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/11",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/12",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/13",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/14",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/15",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/16",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/17",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/18",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/19",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/20",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/21",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/22",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/23",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/24",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/25",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/26",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/27",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/28",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/29",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/30",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/31",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/32",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/33",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/34",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/35",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/49",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/50",caption="Dasturchi @Firdavs_Programmer")
    	await message.reply_document(document = "https://t.me/apklar_kitob_baza/51",caption="Dasturchi @Firdavs_Programmer")


    elif message.text =="📚Badiiy adabiyotlar📚":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menubooks)

    elif message.text =="🧑‍💻Bot dasturchisi🧑‍💻":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuDasturchilar)

    elif message.text =="Pdf kitoblar":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuAdabiyotlar)

    elif message.text =="<-Orqaga🔙":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.mainMenu)

    elif message.text =="Audio kitoblar":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menuAudioBooks)

    elif message.text =="🔙 orqaga":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.menubooks)


    elif message.text == "◀️Bosh menyu▶️":
        await bot.send_message(message.from_user.id, message.text, reply_markup=nav.mainMenu)
        
    elif message.text == "🤖Bizning Botlarimiz🤖":
        await bot.send_message(message.from_user.id, message.text, reply_markup = nav.menuBots)


    elif message.text =="📹Videodarsliklar📹":
        await bot.send_message(message.from_user.id, message.text, reply_markup=vid.menuVideo)

    elif message.text == "🔢1-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu1sinf)

    elif message.text == "🔢2-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu2sinf)

    elif message.text =="🔢3-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu3sinf)

    elif message.text =="🔢4-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu4sinf)

    elif message.text =="🔢5-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu5sinf)

    elif message.text =="🔢6-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu6sinf)

    elif message.text =="🔢7-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu7sinf)

    elif message.text =="🔢8-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu8sinf)

    elif message.text =="🔢9-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu9sinf)

    elif message.text =="🔢10-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu10sinf)

    elif message.text =="🔢11-sinf🔢":
        await bot.send_message(message.from_user.id, message.text, reply_markup= nav.menu11sinf)

    

    if message.text=="📖1-sinf Tarbiya📖":
        await message.reply_document(document ="https://t.me/firdavsbek1551/218",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖1-sinf Matematika📖":
        await message.reply_document(document = "https://t.me/firdavsbek1551/227",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖1-sinf Alifbe📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/231",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖1-sinf Yozuv daftari📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/219",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖1-sinf Matematika daftari📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/228",caption="Dasturchi @Firdavs_Programmer")



    elif message.text == "📖1-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/223",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖1-sinf Tabiiy fan📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/232",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖1-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/230",caption="Dasturchi @Firdavs_Programmer")


    elif message.text == "📖1-sinf Tasviriy san'at📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/221",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖1-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/220",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖1-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/229",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖1-sinf Musiqa📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/226",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖2-sinf Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/211",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖2-sinf Matematika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/205",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖2-sinf oqish📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/209",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖2-sinf Rus tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/212",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖2-sinf Matematika daftari📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/206",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖2-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/210",caption="Dasturchi @Firdavs_Programmer")
    
    elif message.text == "📖2-sinf Tabiiy fan📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/204",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖2-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/207",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖2-sinf Tasviriy san'at📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/213",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖2-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/214",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖2-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/200",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖3-sinf Tarbiya":
        await message.reply_document(document="https://t.me/firdavsbek1551/197",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖3-sinf Matematika":
        await message.reply_document(document="https://t.me/firdavsbek1551/195",caption="Dasturchi @Firdavs_Programmer")

    
    elif message.text == "📖3-sinf O'qish":
        await message.reply_document(document="https://t.me/firdavsbek1551/193",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖3-sinf Musiqa":
        await message.reply_document(document="https://t.me/firdavsbek1551/196",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖3-sinf rus tili":
        await message.reply_document(document="https://t.me/firdavsbek1551/201",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖3-sinf Ona tili":
        await message.reply_document(document="https://t.me/firdavsbek1551/192",caption="Dasturchi @Firdavs_Programmer")


    elif message.text == "📖3-sinf Tabiiy fan":
        await message.reply_document(document="https://t.me/firdavsbek1551/203",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖3-sinf Ingliz tili":
        await message.reply_document(document="https://t.me/firdavsbek1551/198",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖3-sinf Tasviriy san'at":
        await message.reply_document(document="https://t.me/firdavsbek1551/198",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖3-sinf Texnologiya":
        await message.reply_document(document="https://t.me/firdavsbek1551/201",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖3-sinf Jismoniy Tarbiya":
        await message.reply_document(document="https://t.me/firdavsbek1551/200",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖4-sinf Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/178",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖4-sinf Matematika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/181",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖4-sinf O'qish📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/189",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖4-sinf Musiqa📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/182",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖4-sinf Rus tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/178",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖4-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/179",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖4-sinf Tabiiy fan📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/186",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖4-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/188",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖4-sinf Tasviriy san'at📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/180",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖4-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/183",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖4-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/187",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/156",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Matematika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/176",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Geografiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/161",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Informatika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/163",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Matematika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/176",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/169",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Adabiyot 1":
        await message.reply_document(document="https://t.me/firdavsbek1551/156",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Rus tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/157",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Adabiyot 2📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/165",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Musiqa📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/173",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Tabiiy fan📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/158",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/164",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Tasviriy san'at📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/171",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/162",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖5-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/168",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖6-sinf Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/144",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖6-sinf Matematika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/147",caption="Dasturchi @Firdavs_Programmer")


    elif message.text == "📖6-sinf Botanika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/141",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖6-sinf Adabiyot 1📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/139",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖6-sinf Adabiyot 2📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/140",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖6-sinf Fizika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/142",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖6-sinf Tabiiy fan📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/141",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖6-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/145",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖6-sinf Tasviriy san'at📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/152",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖6-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/154",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖6-sinf Musiqa📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/148",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖6-sinf Informatika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/144",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖6-sinf Geografiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/143",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖6-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/151",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/119",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf Fizika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/119",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf Adabiyot📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/137",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf Zoologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/123",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf Algebra📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/134",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/133",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf Kimyo📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/131",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/130",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf Tasviriy san'at📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/125",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/124",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/128",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf Geometriya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/136",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf Geografiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/129",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf O'zb tarix📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/121",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖7-sinf Jahon tarixi📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/120",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf Algebra📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/100",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf Geografiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/105",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf Informatika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/106",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf Adabiyot📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/116",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/109",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf Biologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/114",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/108",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf Kimyo📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/114",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/114",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/128",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf Fizika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/102",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf Rus tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/110",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf chizmachilik📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/101",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf Geometriya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/104",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf DHA📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/112",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf O'zbekiston Tarixi📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/111",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖8-sinf Jahon tarixi📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/110",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/96",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Algebra📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/94",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Adabiyot📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/88",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Fizika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/85",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf O'zbekiton tarixi📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/81",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/80",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Geografiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/93",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/92",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf chizmachilik📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/67",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Texnologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/82",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/92",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Biologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/84",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Kimyo📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/76",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf DHA📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/91",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Informatika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/96",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Rus tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/95",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Geometriya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/87",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖9-sinf Jahon tarixi📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/75",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Bilogiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/17",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Algebra📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/22",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Adabiyot📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/28",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/23",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Geografiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/58",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Rus tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/26",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Biologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/17",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/19",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Manaviyat asoslari📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/60",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "10-sinf Kimyo📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/24",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Din tarixi📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/18",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Jahon Tarix📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/20",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Tarix📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/25",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Matematika 2📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/21",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Adabiyot 2📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/27",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf DHA📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/55",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf chqbt📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/56",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Fizika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/57",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Informatika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/59",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖10-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/56",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf DHA📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/42",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf Rus tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/8",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf Din Tarix📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/43",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf Algebra📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/4",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf Adabiyot📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/41",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf Jahon tarix📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/3",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf Ona tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/15",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf Kimyo📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/9",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf Ingliz tili📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/13",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf Fizika📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/12",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf Jismoniy Tarbiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/41",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf Astronomiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/10",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf Kimyo📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/9",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf Biologiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/11",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📖11-sinf Geografiya📖":
        await message.reply_document(document="https://t.me/firdavsbek1551/10",caption="Dasturchi @Firdavs_Programmer")
# ---------->>>>>>>>>>>><<<<<<<<<<< Badiiy Adabiyotlar -------------------->>>>>>>>><<<<<<<<<<
    elif message.text == "📚Sariq devni minib📚":
        await message.reply_document(document="https://t.me/firdavsbek1551/242",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📚Mungli ko'zlar📚":
        await message.reply_document(document="https://t.me/firdavsbek1551/240",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📚Sariq devning o'limi📚":
        await message.reply_document(document="https://t.me/firdavsbek1551/243",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📚O'tkan kunlar📚":
        await message.reply_document(document="https://t.me/firdavsbek1551/247",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📚Quyonlar saltanati📚":
        await message.reply_document(document="https://t.me/firdavsbek1551/241",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "📚Mehrobdan Chayon📚":
        await message.reply_document(document="https://t.me/firdavsbek1551/245",caption="Dasturchi @Firdavs_Programmer")



        # AUDIO

    elif message.text == "Me'mor":
        await message.reply_document(document="https://t.me/firdavsbek1551/384",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Taras bulba":
        await message.reply_document(document="https://t.me/firdavsbek1551/383",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Erka qizning qismati":
        await message.reply_document(document="https://t.me/firdavsbek1551/382",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Garov":
        await message.reply_document(document="https://t.me/firdavsbek1551/381",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Shum bola":
        await message.reply_document(document="https://t.me/firdavsbek1551/380",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Jinlar bazmi":
        await message.reply_document(document="https://t.me/firdavsbek1551/379",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Uloqda":
        await message.reply_document(document="https://t.me/firdavsbek1551/375",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Qurigan daraxt":
        await message.reply_document(document="https://t.me/firdavsbek1551/388",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Kashfiyot":
        await message.reply_document(document="https://t.me/firdavsbek1551/390",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Yutuq":
        await message.reply_document(document="https://t.me/firdavsbek1551/386",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Orziqib kutaman ertani":
        await message.reply_document(document="https://t.me/firdavsbek1551/393",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "G'ayri oddiy ong mo'jizalari":
        await message.reply_document(document="https://t.me/firdavsbek1551/395",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Saodatga eltuvchi bilim":
        await message.reply_document(document="https://t.me/firdavsbek1551/396",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Daydi qizning daftari":
        await message.reply_document(document="https://t.me/firdavsbek1551/397",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Yo'qolgan dunyo":
        await message.reply_document(document="https://t.me/firdavsbek1551/398",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Sarvqomat dilbarim":
        await message.reply_document(document="https://t.me/firdavsbek1551/399",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "To'rt ulus tarixi":
        await message.reply_document(document="https://t.me/firdavsbek1551/400",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Soliha ayollar":
        await message.reply_document(document="https://t.me/firdavsbek1551/401",caption="Dasturchi @Firdavs_Programmer")
    
    elif message.text == "Hikmatli latifalar":
        await message.reply_document(document="https://t.me/firdavsbek1551/402",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Baxt qasri":
        await message.reply_document(document="https://t.me/firdavsbek1551/403",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Sarmoyador":
        await message.reply_document(document="https://t.me/firdavsbek1551/404",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Osmondan tushgan pul":
        await message.reply_document(document="https://t.me/firdavsbek1551/405",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Donolar suhbati":
        await message.reply_document(document="https://t.me/firdavsbek1551/406",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Uch oltin gisht":
        await message.reply_document(document="https://t.me/firdavsbek1551/407",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Saylanma":
        await message.reply_document(document="https://t.me/firdavsbek1551/408",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Salomatlik sirlari":
        await message.reply_document(document="https://t.me/firdavsbek1551/409",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Meshpolvon jangga otlandi":
        await message.reply_document(document="https://t.me/firdavsbek1551/410",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Amerika fojiasi":
        await message.reply_document(document="https://t.me/firdavsbek1551/411",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Bo'ston ul-orifiyn":
        await message.reply_document(document="https://t.me/firdavsbek1551/412",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Shahzoda va Gado":
        await message.reply_document(document="https://t.me/firdavsbek1551/413",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Daryolar tutashgan joyda":
        await message.reply_document(document="https://t.me/firdavsbek1551/414",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Champo otli ilon":
        await message.reply_document(document="https://t.me/firdavsbek1551/415",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Eynshteyn bilan Iblisvachcha":
        await message.reply_document(document="https://t.me/firdavsbek1551/416",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Bola Alisher":
        await message.reply_document(document="https://t.me/firdavsbek1551/417",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Oq marmar":
        await message.reply_document(document="https://t.me/firdavsbek1551/418",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Cho'ri":
        await message.reply_document(document="https://t.me/firdavsbek1551/419",caption="Dasturchi @Firdavs_Programmer")


    elif message.text == "Cho'l burguti":
        await message.reply_document(document="https://t.me/firdavsbek1551/420",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Garri Potter va ajal tuhfalari":
        await message.reply_document(document="https://t.me/firdavsbek1551/421",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Garri Potter va falsafiy tosh":
        await message.reply_document(document="https://t.me/firdavsbek1551/422",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Daftar hoshiyasidagi bitiklar":
        await message.reply_document(document="https://t.me/firdavsbek1551/423",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Ichindagi ichindadir":
        await message.reply_document(document="https://t.me/firdavsbek1551/424",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Bizning shaharda o'g'ri yo'q":
        await message.reply_document(document="https://t.me/firdavsbek1551/425",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Sudxo'rning o'limi":
        await message.reply_document(document="https://t.me/firdavsbek1551/426",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Zulmat ichra nur":
        await message.reply_document(document="https://t.me/firdavsbek1551/427",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Kech kuz":
        await message.reply_document(document="https://t.me/firdavsbek1551/428",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Odamiylik mulki":
        await message.reply_document(document="https://t.me/firdavsbek1551/429",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Bo'ri bolalarini qanday o'rgatadi":
        await message.reply_document(document="https://t.me/firdavsbek1551/430",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Futbol qiroli":
        await message.reply_document(document="https://t.me/firdavsbek1551/431",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Ey farzand":
        await message.reply_document(document="https://t.me/firdavsbek1551/432",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Avlodlar dovoni":
        await message.reply_document(document="https://t.me/firdavsbek1551/433",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Ajab dunyo":
        await message.reply_document(document="https://t.me/firdavsbek1551/434",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Yolg'onchi yor":
        await message.reply_document(document="https://t.me/firdavsbek1551/436",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Qiz bolaga tosh otmang":
        await message.reply_document(document="https://t.me/firdavsbek1551/437",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Boy bo'lishning 10ta siri":
        await message.reply_document(document="https://t.me/firdavsbek1551/438",caption="Dasturchi @Firdavs_Programmer")


    elif message.text == "Kalila va Dimna":
        await message.reply_document(document="https://t.me/firdavsbek1551/439",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Biz millionermiz":
        await message.reply_document(document="https://t.me/firdavsbek1551/440",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Don Kristobalning xatosi":
        await message.reply_document(document="https://t.me/firdavsbek1551/441",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Daydi qizning daftari":
        await message.reply_document(document="https://t.me/firdavsbek1551/444",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Bu dunyoda o'lib bo'lmaydi":
        await message.reply_document(document="https://t.me/firdavsbek1551/445",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Kapitan qizi":
        await message.reply_document(document="https://t.me/firdavsbek1551/446",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Ona haqida sherlar":
        await message.reply_document(document="https://t.me/firdavsbek1551/447",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Pul topishning ulkan siri":
        await message.reply_document(document="https://t.me/firdavsbek1551/448",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Devona":
        await message.reply_document(document="https://t.me/firdavsbek1551/449",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Besh bolali yigitcha":
        await message.reply_document(document="https://t.me/firdavsbek1551/450",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Qo'rqmang onaginam":
        await message.reply_document(document="https://t.me/firdavsbek1551/453",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Yo'qolgan Dunyo":
        await message.reply_document(document="https://t.me/firdavsbek1551/454",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Boy ota kambag'al ota":
        await message.reply_document(document="https://t.me/firdavsbek1551/455",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Oygul bilan Baxtiyor":
        await message.reply_document(document="https://t.me/firdavsbek1551/456",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Ikki karra ikki Besh":
        await message.reply_document(document="https://t.me/firdavsbek1551/457",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "Gulliverning sayohatlari":
        await message.reply_document(document="https://t.me/firdavsbek1551/442",caption="Dasturchi @Firdavs_Programmer")

    elif message.text == "":
        await message.reply_document(document="")

    elif message.text == "":
        await message.reply_document(document="")






if __name__ =="__main__":
    executor.start_polling(dp, skip_updates=True)


















#  _____  _            _                     _            _
# |  ___|(_) _ __   __| |  __ _ __   __ ___ | |__    ___ | | __
# | |_   | || '__| / _` | / _` |\ \ / // __|| '_ \  / _ \| |/ /
# |  _|  | || |   | (_| || (_| | \ V / \__ \| |_) ||  __/|   <
# |_|    |_||_|    \__,_| \__,_|  \_/  |___/|_.__/  \___||_|\_\


#  ____
# |  _ \  _ __   ___    __ _  _ __   __ _  _ __ ___   _ __ ___    ___  _ __
# | |_) || '__| / _ \  / _` || '__| / _` || '_ ` _ \ | '_ ` _ \  / _ \| '__|
# |  __/ | |   | (_) || (_| || |   | (_| || | | | | || | | | | ||  __/| |
# |_|    |_|    \___/  \__, ||_|    \__,_||_| |_| |_||_| |_| |_| \___||_|
#                      |___/


