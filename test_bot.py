import telebot
api ='1314035904:AAHC-Zhdd0RAEbhVtze5aDbdjbXsKF_qJBs'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Hai Para Same IT Developer, Gmana Kabarnya Bro")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,"Tonton Video Terbaru dari Chanel kami")

print('bot Sedang Jalan')
bot.polling()
