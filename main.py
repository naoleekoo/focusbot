import telegram
from telegram.ext import *

token = "5943385111:AAFZkC5P-OynfrcqForrBIwB9QofEFSBEV0"

updater = Updater("5943385111:AAFZkC5P-OynfrcqForrBIwB9QofEFSBEV0", use_context= True)

dispatcher = updater.dispatcher
bot = telegram.Bot(token = token)

def start(update, context):
    update.message.reply_text("Baga nagaan gara bootii telegraami FOCUS Finfinnee dhufte!")
def sagantaalee(update, context):
    update.message.reply_text( " ✅ Sagantaan Waaqeffannaa Idilee Feelooshippii FOCUS Finfinnee"
                                "\n🗓 Jimaata"
                                "\n⏰ 11:30 - 1:45"
                                "\n🏥 Waldaa G/G/M Waaqayyoo"

)
def gartuulee(update, context):
    update.message.reply_text("Gartuulen Feeloshiippii keenya keessa jiran"
                              "\n ✅ Gartuu Dhuga-bahuumsaa"
                              "\n ✅ Gartuu Qu'annaa Macaafa Qulqulluu"
                              "\n ✅ Gartuu Kadhannaa"
                              "\n ✅ Gartuu Toosiftootaa"
                              "\n ✅ Gartuu Faarfattootaa"
                              "\n ✅ Gartuu Hawaasummaa"
                              "\n ✅ Gartuu LAD/ODA"
                              )
def feed(update,context):
    # send reply to the user
    message = update.message.text
    message = str(message)
    user = update.message.chat
    bot.send_message(chat_id=update.message.chat_id,
                     text="Eebbifami {}. ".format(user['first_name']))
    # forward user message to group
    # note: group ID with the negative sign
    bot.forward_message(chat_id='-886873334',
                    from_chat_id=update.message.chat_id,
                    message_id=update.message.message_id)
def ergaaf(update, context):
    update.message.reply_text("Ergaa kee erga barreessitee booda ergi ")
    dispatcher.add_handler(MessageHandler(Filters.text, feed))

def error(update, context):
    print(f'Update {update} caused error {context.error}')

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("sagantaalee", sagantaalee))
dispatcher.add_handler(CommandHandler("gartuulee", gartuulee))
dispatcher.add_handler(CommandHandler("ergaaf", ergaaf))
dispatcher.add_handler(MessageHandler(Filters.text, feed))
updater.dispatcher.add_error_handler(error)
updater.start_polling()
updater.idle()






