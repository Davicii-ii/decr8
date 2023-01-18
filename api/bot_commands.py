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

from telegram.ext import CallbackContext

from api.variables import *
from api.bot_error import *

from telegram.utils import (
    helpers
    )

def start(update: Update, context: CallbackContext) -> None:
    """Start bot"""

    global COUNT

    COUNT = 0
    
    reply_keyboard = [
        ['/start'],['/queue', "/scdl"],['/help']
    ]
    
    """Send a deep-linked URL when the command /start is issued."""
    bot = context.bot
    
    url = helpers.create_deep_linked_url(
        bot.get_me().username,
        DECR8,
        group=True
        )
    
    text = ("👺" "{} items found".format(len(data)))
    
    update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            parse_mode=ParseMode.MARKDOWN,
            one_time_keyboard=True
        )
    )
    
    return STAGE1

def add(update: Update, context: CallbackContext) -> None:

    global COUNT
    
    reply_keyboard = [
        ["/queue"],
        ["/sub", "/add"]
    ]

    COUNT += 1

    update.message.reply_text(
        "queue {} song(s)".format(COUNT),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard),
        parse_mode=ParseMode.MARKDOWN
    )

def sub(update: Update, context: CallbackContext) -> None:

    global COUNT

    reply_keyboard = [
        ["/queue"],
        ["/sub", "/add"]
    ]
    help_keyboard = [
        ["/add"]
    ]

    if COUNT <= 1:
        update.message.reply_text(
            "queue cant be < {}. /add instead".format(COUNT),
            reply_markup=ReplyKeyboardMarkup(help_keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        COUNT -= 1
        update.message.reply_text(
            "queue {} song(s)\nuse /add for more".format(COUNT),
            reply_markup=ReplyKeyboardMarkup(reply_keyboard),
            parse_mode=ParseMode.MARKDOWN
        )


def queue(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /next is issued."""

    global COUNT
    
    if COUNT < 1:
        COUNT = 1

    attempts = 0
    max_attempts = 3

    for i in range(COUNT):
        try:
            for i in range(COUNT):
                url = "https://t.me/crateofnotsodasbutmusic/{}".format(
                    random.choice(list(data.values())))
                
                reply_keyboard = [
                    ["/sub", "/add"],
                    ["/queue"],
                    ["/start"]
                ]
                
                update.message.reply_audio(
                    "{}".format(url),
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=ReplyKeyboardMarkup(
                        reply_keyboard,
                        one_time_keyboard=True
                    )
                )
               
                break
        except (BadRequest) as e:
            attempts += 1
            if attempts >= max_attempts:
                break

def run_update(update: Update, context: CallbackContext):
    command = "python3 update_history.py"
    result = os.popen(command).read()  # Run the command and get the output
    update.message.reply_text(result)

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text("/next Add to playlist.")
    
