import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "1307013162:AAE6YjEfSNuqXLPE6eMSF7dnIvXBZMVvetg"

def start(bot, context):
    bot.message.reply_text("Hello, boozer!")

def message(bot, context):
    text = bot.message.text
    count = len(text)
    response = "In your message {} symbols."
    bot.message.reply_text(response.format(count))

def math(bot, context):
    value = "".join(context.args)
    res = eval(value)
    bot.message.reply_text(str(res))

def picture(bot, context):
    file_info = bot.get_file(context.photo[0].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    pict = '/home/hanna/TMS/projects/bot_le/' + context.photo[0].file_id
    with open (pict, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.message.reply_text('SAVED')
   
        
def run():
    bot = Updater(TOKEN, use_context=True)
    bot.dispatcher.add_handler(CommandHandler("start", start))
    bot.dispatcher.add_handler(CommandHandler("math", math))
    bot.dispatcher.add_handler(MessageHandler(Filters.photo, picture))
    bot.dispatcher.add_handler(MessageHandler(Filters.text, message))
    bot.start_polling()
    bot.idle()

if __name__ == "__main__":
    run()