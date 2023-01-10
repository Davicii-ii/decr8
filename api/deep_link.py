from telegram import Update
from telegram.ext import CallbackContext
from api.variables import *

import api

def deep_linked_level_1(update: Update, context: CallbackContext) -> None:
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

def deep_linked_level_2(update: Update, context: CallbackContext) -> None:
    """Reached through the SO_COOL payload"""
    bot = context.bot
    
    url = helpers.create_deep_linked_url(
        bot.get_me().username,
        USING_ENTITIES
    )

    text = " ""[▶️ STOP BOT]({}).".format(url)
    update.message.reply_text(
        text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True
    )

def deep_linked_level_3(update: Update, context: CallbackContext) -> None:
    """Reached through the USING_ENTITIES payload"""
    payload = context.args
    update.message.reply_text(
        "/queue",
        parse_mode=ParseMode.MARKDOWN
    )


def stage1(update: Update, context: CallbackContext) -> int:

    return STAGE2

def stage2(update: Update, context: CallbackContext) -> int:

    return STAGE3

def stage3(update: Update, context: CallbackContext) -> int:

    return STAGE4

def stage4(update: Update, context: CallbackContext) -> int:

    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:

    return ConversationHandler.END