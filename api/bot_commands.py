from api.imports import *
from api.variables import *
from api.bot_error import *

COUNT = 0

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start bot"""

    global COUNT
    
    COUNT = 1
    
    reply_keyboard = [
        ["/start"],
        ["/queue", "/queue_mix"],
        ["/help"]
    ]
    
    """Send a deep-linked URL when the command /start is issued."""
    bot = context.bot
    
    url = helpers.create_deep_linked_url(
        bot.username,
        DECR8,
        group=True
        )
    
    text = ("👺" "{} items found".format(len(data)))
    
    await update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True
        )
    )
    
    return STAGE1

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    global COUNT
    
    reply_keyboard = [
        ["/queue", "/queue_mix"],
        ["/sub", "/add"]
    ]

    COUNT += 1

    await update.message.reply_text(
        "queue {} song(s)".format(COUNT),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard),
        parse_mode=ParseMode.MARKDOWN
    )

async def sub(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    global COUNT

    reply_keyboard = [
        ["/queue", "/queue_mix"],
        ["/sub", "/add"]
    ]
    help_keyboard = [
        ["/add"]
    ]

    if COUNT < 1:
        await update.message.reply_text(
            "queue cant be < {}. /add instead".format(COUNT),
            reply_markup=ReplyKeyboardMarkup(help_keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        COUNT -= 1
        await update.message.reply_text(
            "queue {} song(s)\nuse /add for more".format(COUNT),
            reply_markup=ReplyKeyboardMarkup(reply_keyboard),
            parse_mode=ParseMode.MARKDOWN
        )

async def queue(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
        try:
            await update.message.reply_audio(
                "{}".format(url),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=ReplyKeyboardMarkup(
                    reply_keyboard,
                    one_time_keyboard=True
                )
            )
        except AttributeError as e:
            continue
        
async def queue_mix(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
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
            await update.message.reply_audio(
                "{}".format(url),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=ReplyKeyboardMarkup(
                    reply_keyboard,
                    one_time_keyboard=True
                )
            )
        except BadRequest as e:
            continue
        
async def run_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = "python3 get_history.py"
    result = os.popen(command).read()  # Run the command and get the output
    await update.message.reply_text(f"{result}\n done.")
    
async def help_command(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("/next Add to playlist.")

