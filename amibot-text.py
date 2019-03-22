from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction


# define a command handler. Command handlers usually take two arguments:
# bot and update
def start(bot, update):
    update.message.reply_text("Hello!")


# the non-command handler
def echo(bot, update):
    # simulate typing from the bot
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)

    # get the message from the user
    repeat_text = update.message.text
    # send the message back
    update.message.reply_text(repeat_text)
    # alternative way: bot.sendMessage(update.message.chat_id, repeat_text)


def main():
    """
    The AmIBot will greet you and it will repeat everything you type
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

    # on non-command textual messages - echo the original message
    dp.add_handler(MessageHandler(Filters.text, echo))

    # start the bot
    updater.start_polling()

    # run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
