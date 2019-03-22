from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction
from gtts import gTTS


# define a command handler. Command handlers usually take two arguments:
# bot and update
def start(bot, update):
    update.message.reply_text("Hello!")


# the non-command handler
def echo(bot, update):
    # get the chat id
    chat_id = update.message.chat_id
    # simulate the upload of an audio file from the bot
    bot.sendChatAction(chat_id, ChatAction.UPLOAD_AUDIO)

    # get the message from the user
    repeat_text = update.message.text

    # convert the textual message into audio
    tts = gTTS(text=repeat_text, lang="en")
    tts.save("echo.mp3")
    # send the message back
    bot.sendVoice(chat_id=chat_id, voice=open("echo.mp3", "rb"))


def main():
    """
    The AmIBot will greet you and it will repeat (by voice) everything you type
    """
    # create the EventHandler and pass it your bot's token
    # N.B. this token is not valid!
    updater = Updater("712562135:AAH3Aa_l5UONCDmBENQQT6D4QzYmsC7_9Zw")

    # get the dispatcher to register handlers
    dp = updater.dispatcher

    # add the command handler for the "/start" command
    dp.add_handler(CommandHandler("start", start))
    # another example of CommandHandler...
    # dp.add_handler(CommandHandler("help", help))

    # on non-command textual messages - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # start the bot
    updater.start_polling()

    # run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
