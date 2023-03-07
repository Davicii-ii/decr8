from api import imports
from api.variables import *

import api

async def deep_linked_level_1(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Reached through the CHECK_THIS_OUT payload"""
    bot = context.bot
    try:
        result_id = [
            k
            for k, v in data.items()
        ]
        track_url = "https://t.me/crateofnotsodasbutmusic/{}".format(
            random.choice(result_id)
        )
        for i in range(1):
            await update.message.reply_text(
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
    
    await update.message.reply_text(
        text,
        reply_markup=keyboard
    )

async def deep_linked_level_2(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Reached through the SO_COOL payload"""
    bot = context.bot
    
    url = helpers.create_deep_linked_url(
        bot.get_me().username,
        USING_ENTITIES
    )

    text = " ""[▶️ STOP BOT]({}).".format(url)
    await update.message.reply_text(
        text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True
    )

async def deep_linked_level_3(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Reached through the USING_ENTITIES payload"""
    payload = context.args
    await update.message.reply_text(
        "/queue",
        parse_mode=ParseMode.MARKDOWN
    )
