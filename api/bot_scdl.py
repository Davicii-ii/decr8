from telegram import (
    Update,
    InlineQueryResultAudio,
    InlineQueryResultArticle,
    InputTextMessageContent,
    ParseMode,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from telegram.ext import (
    Updater,
    InlineQueryHandler,
    CommandHandler,
    ConversationHandler,
    CallbackQueryHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)

from api.variables import *
from api.bot_error import *

from uuid import uuid4

def scdl_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued.""" 

    reply_keyboard = [["/start"],["t.me/decr8test_bot"]]
    update.message.reply_text(
        "👺",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard),
        parse_mode=ParseMode.MARKDOWN
    )
