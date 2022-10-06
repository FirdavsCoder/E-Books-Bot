@dp.message_handler(text =  "statistika")
async def statistics(message: types.Message):
    connect = sqlite3.connect('./data.db')
    cursor = connect.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    followers = cursor.fetchone()[0]
  

    await message.answer(f"📊 Statistika\n"
                         f"🫂 Botdagi jami foydalanuvchilar soni:  {followers}\n")
                         
                         
                         
                         






connect = sqlite3.connect('./data.db')
        cursor = connect.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users ("key"  INTEGER,"user_id"  INTEGER,"date"  INTEGER);""")
        if cursor.execute(f"""SELECT user_id FROM users WHERE user_id = {message.chat.id}""").fetchone() == None:
            sana = datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%d-%m-%Y %H:%M')
            cursor.execute(
                "INSERT INTO users (user_id, date) VALUES ('{user_id}', '{sana}')".format(user_id=message.chat.id,
                                                                                          sana=sana))
            connect.commit()