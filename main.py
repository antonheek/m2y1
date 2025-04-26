
@bot.message_handler(commands=['mem, memes'])
def mem(message): 
    global memes 
    words = message.text.split()
    if len(words) > 1:
        number_mem = words[1] - 1
        if 0 <= number_mem < len(number_mem):
            with open(f"img/{memes[number_mem]}", "rb") as f:
                return  bot.send_photo(message.chat.id, f)
        else:
            return bot.send_message(message.chat.id, "мема с таким номером нет")
    mems =random.choice(memes)
    with open(f"img/{mems}", "rb") as f:
         bot.send_photo(message.chat.id, f)
    memes.remove(mems)
    if memes == []:
        memes = os.listdir("./img")
