from api.imports import *
from api.variables import *
from api.bot_error import *

COUNT = 0

def start(update: Update, context: CallbackContext) -> None:
    """Start bot"""

    global COUNT
    
    COUNT = 1
    
    reply_keyboard = [
        ["/start"],["/queue", "/queue_mix"], ["/scdl"], ["/help"]
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
        ["/queue", "/queue_mix"],
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
        ["/queue", "/queue_mix"],
        ["/sub", "/add"]
    ]
    help_keyboard = [
        ["/add"]
    ]

    if COUNT < 1:
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
         
    msg_id = []

    for k, v in data.items():
        msg_id.append(k)

    for i in range(COUNT):
        url = "https://t.me/crateofnotsodasbutmusic/{}".format(
            random.choice(msg_id))
        
        reply_keyboard = [
            ["/sub", "/add"],
            ["/queue", "/queue_mix"],
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
        
def queue_mix(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /next is issued."""
    
    global COUNT
        
    msg_id = []

    for k, v in data.items():
        if v.get("duration") > 600 and v.get("duration") < 18000:
            msg_id.append(k)

    for i in range(COUNT):
        url = "https://t.me/crateofnotsodasbutmusic/{}".format(
            random.choice(msg_id))
        
        reply_keyboard = [
            ["/sub", "/add"],
            ["/queue", "/queue_mix"],
            ["/start"]
        ]
        try:
            update.message.reply_audio(
                "{}".format(url),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=ReplyKeyboardMarkup(
                    reply_keyboard,
                    one_time_keyboard=True
                )
            )
        except BadRequest as e:
            continue
        
def run_update(update: Update, context: CallbackContext):
    command = "python3 update_history.py"
    result = os.popen(command).read()  # Run the command and get the output
    update.message.reply_text(result)
    
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text("/next Add to playlist.")

