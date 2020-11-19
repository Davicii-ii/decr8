# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging, random, os, re, json
from uuid import uuid4

from telegram import (
    InlineQueryResultAudio,
    ParseMode,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from telegram.ext import (
    Updater,
    InlineQueryHandler,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    Filters
)

from telegram.utils import (
    helpers
    )

from telegram.utils.helpers import escape_markdown
from telegram.error import TelegramError, BadRequest

from pyrogram import Client

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

decr8 = -1001280481543
decr8_link = "t.me/crateofnotsodasbutmusic"

# Define constants that will allow us to reuse the deep-linking parameters.
DECR8 = 'decr8'
USING_ENTITIES = 'using-entities-here'
SO_COOL = 'so-cool'


# dev mode

logger.info("Loading json")
with open("/home/ayuko/decr8/res/decr8_data.json", "r", encoding="utf-8") as f:
    d = json.load(f)
    logger.info("Found {} items.".format(len(d.values())))

def start(update, context):
    update.message.reply_text(
        "/next : ➕ queue playlist. \n/help : ⚙️ show options.\n\n""🔌[dec8]({})".format(decr8_link),
        parse_mode=ParseMode.MARKDOWN
        )
    
    """Send a deep-linked URL when the command /start is issued."""
    bot = context.bot

    url = helpers.create_deep_linked_url(
        bot.get_me().username,
        DECR8,
        group=True
    )

    text = "👺 ""[Go tell the people about me!]({})".format(url)
    
    update.message.reply_text(
        text,
        parse_mode=ParseMode.MARKDOWN
    )

def deep_linked_level_1(update, context):
    """Reached through the CHECK_THIS_OUT payload"""
    bot = context.bot
    try:
        result_id = [
            v
            for k, v in d.items()
        ]
        track_url = "https://t.me/crateofnotsodasbutmusic/{}".format(
            random.choice(result_id)
        )
        for i in range(1):
            update.message.reply_text(
                "::*decr8* ""[🎧]({})".format(track_url),
                parse_mode=ParseMode.MARKDOWN
            )
    except (BadRequest) as e:
        logger.warning(e)                                                      

    url = helpers.create_deep_linked_url(
        bot.get_me().username,
        SO_COOL
    )
    
    text = (
        "let's go to the private chat for more.\ni will not spam here."
    )
    
    keyboard = InlineKeyboardMarkup.from_button(
        InlineKeyboardButton(
            text='go to bot chat',
            url=url
        )
    )
    
    update.message.reply_text(
        text,
        reply_markup=keyboard
    )

def deep_linked_level_2(update, context):
    """Reached through the SO_COOL payload"""
    bot = context.bot
    
    url = helpers.create_deep_linked_url(
        bot.get_me().username,
        USING_ENTITIES
    )

    text = " ""[▶️ CLICK HERE]({}).".format(url)
    update.message.reply_text(
        text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True
    )

def deep_linked_level_3(update, context):
    """Reached through the USING_ENTITIES payload"""
    payload = context.args
    update.message.reply_text(
        "/next",
        parse_mode=ParseMode.MARKDOWN
    )

def _next(update, context):
    """Send a message when the command /next is issued."""
    try:
        for i in range(
                min(d.values()),
                max(d.values()),
                max(d.values())//min(d.values())**2
        ):
            url = "https://t.me/crateofnotsodasbutmusic/{}".format(
                random.choice(list(d.values())))

            keyboard = InlineKeyboardMarkup.from_button(
                InlineKeyboardButton(
                    text="open kwa decr8!",
                    url=url
                )
            )       
            
            update.message.reply_audio(
                "{}".format(url),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=keyboard
            )

    except (BadRequest) as e:
        logger.warning(e)
    
    update.message.reply_text(
        "❌\n\n*/next*\n\n⭕️",
        parse_mode=ParseMode.MARKDOWN
    )

def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("/next Add 10 tracks to playlist.")

def search(update, context):
    """Search the user's message."""
    result_id = [
        v
        for k, v in d.items()
        if re.search(update.message.text, k, re.IGNORECASE)
    ]
    
    result_title = [
        k
        for k, v in d.items()
        if re.search(update.message.text, k, re.IGNORECASE)
        ]
    
    url = "https://t.me/crateofnotsodasbutmusic/{}".format(                   
                random.choice(result_id)
        )
    
    for i in range(1):
        update.message.reply_text(
            " ""[{}]({})".format("found this.", url),
            parse_mode=ParseMode.MARKDOWN
            )

def inlinequery(update, context):
    """Handle the inline query."""
    query = update.inline_query.query
    for k, v in d.items():
        if k.startswith(query):
            for i in range(
                min(d.values()),
                max(d.values()),
                max(d.values())//min(d.values())**2
        ):
                results = [
                    InlineQueryResultAudio(
                        id=uuid4(),
                        audio_url="https://t.me/crateofnotsodasbutmusic/{}"
                        .format
                        (v),
                        title="{}"
                        .format(k),
                    )
                ]
            update.inline_query.answer(results)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(
        "1266125805:AAFnUPiqc0LiHPWJNlOp2XhfSGsqtu_cEbA", use_context=True
    )

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register a deep-linking handler
    dp.add_handler(
        CommandHandler(
            "start",
            deep_linked_level_1,
            Filters.regex(DECR8)
        )
    )
    
    # This one works with a textual link instead of an URL
    dp.add_handler(
        CommandHandler(
            "start",
            deep_linked_level_2,
            Filters.regex(SO_COOL)
        )
    )

    # We can also pass on the deep-linking payload
    dp.add_handler(
        CommandHandler(
            "start",
            deep_linked_level_3,
            Filters.regex(USING_ENTITIES),
            pass_args=True
        )
    )
    
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("next", _next))
    dp.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(InlineQueryHandler(inlinequery))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
    
if __name__ == "__main__":
    main()
    
