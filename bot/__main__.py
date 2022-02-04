# Importing Required Modules
import logging

from telegram.ext import Updater

from bot.handlers.feedback import add_feedback_handlers
from bot.handlers.request import add_request_handlers
import bot.configs as vars


# Logging Stuff
logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
logging.getLogger().setLevel(logging.INFO)


def error(update, context):
    OWNER_ID = vars.OWNER_ID
    context.bot.send_message(
        chat_id = OWNER_ID,
        text = f"Update {update} caused error {context.error}"
    )
    logging.warning(f"Update {update} caused error {context.error}")


# MAIN STUFF
def main():
    # GETTING VARIABLES
    BOT_TOKEN = vars.BOT_TOKEN
    BASE_URL_OF_BOT = vars.BASE_URL_OF_BOT
    PORT = vars.PORT

    updater = Updater(BOT_TOKEN, workers=100)
    # GET DISPATCHER TO ADD HANDLERS
    dp = updater.dispatcher

    # SETTING HANDLERS
    add_feedback_handlers(dp)
    add_request_handlers(dp)

    dp.add_error_handler(error)

    # STARTING WEBHOOK
    updater.start_webhook(
        listen="0.0.0.0",
        port = PORT,
        url_path = BOT_TOKEN,
        webhook_url = BASE_URL_OF_BOT + BOT_TOKEN
    )

    logging.info("Bot Started...✅")
    updater.idle()




if __name__ == "__main__":

    main()