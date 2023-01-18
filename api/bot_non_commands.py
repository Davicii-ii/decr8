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

def search(update: Update, context: CallbackContext) -> None:
    """Search the user's message."""
    global KEY
    global VAL
    global COUNT
    
    VAL = [
        v
        for k, v in data.items()
        if re.search(update.message.text, k, re.IGNORECASE)
    ]
    KEY = [
        k
        for k, v in data.items()
        if re.search(update.message.text, k, re.IGNORECASE)
    ]
    
    keyboard = [
        [
            InlineKeyboardButton(
                "<",
                callback_data="1"
            ),
            
            InlineKeyboardButton(
                ">",
                callback_data="2"
            ),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    COUNT = 0

    link = re.search(r"(t\.me\/[a-zA-Z0-9_]{5,32})", update.message.text)

    try:
        text = (
            "👺\nResult {} of {}\n ""[{}]({})\n".format(
                KEY.index(KEY[COUNT]),
                len(KEY),
                KEY[COUNT],
                dcr8_url+"{}".format(VAL[COUNT])
            )
        )

        update.message.reply_text(
            text,
            reply_markup=reply_markup,
            parse_mode=ParseMode.MARKDOWN
        )
    except (BadRequest, IndexError) as e:
        if link:
            update.message.reply_text("use this bot to download songs: \nt.me/decr8test_bot")
        else:
            update.message.reply_text("Not found.")
        
def search_buttons(update: Update, context: CallbackContext) -> None:
    global KEY
    global VAL
    global COUNT
    
    query = update.callback_query
    
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer(text="🤖")

    keyboard = [
        [
            InlineKeyboardButton(
                "<",
                callback_data="1"
            ),
            
            InlineKeyboardButton(
                ">",
                callback_data="2"
            ),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        if query.data == '1':
            COUNT -= 1
            text = "👺\nResult {} of {}\n ""[{}]({})\n".format(
                KEY.index(KEY[COUNT]),
                len(KEY),
                KEY[COUNT],
                dcr8_url+"{}".format(VAL[COUNT])
            )

            query.edit_message_text(
                text,
                reply_markup=reply_markup,
                parse_mode=ParseMode.MARKDOWN
            )
        
        elif query.data == '2':
            COUNT += 1
            text = "👺\nResult {} of {}\n ""[{}]({})\n".format(
                KEY.index(KEY[COUNT]),
                len(KEY),
                KEY[COUNT],
                dcr8_url+"{}".format(VAL[COUNT])
            )

            query.edit_message_text(
                text,
                reply_markup=reply_markup,
                parse_mode=ParseMode.MARKDOWN
            )
    except(IndexError, BadRequest):
        update.message.reply_text("Not Found.")
    
def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""

    query = update.inline_query.query
    results = []

    for k, v in data.items():
        if re.search(query, k, re.IGNORECASE):
            results.append(
                InlineQueryResultAudio(
                    id=uuid4(),
                    audio_url="{}{}".format(dcr8_url, v),
                    title="{}".format(k)
                ),
            )
        
    update.inline_query.answer(results, auto_pagination=True)

