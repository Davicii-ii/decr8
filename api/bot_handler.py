from api.imports import *
from api.variables import *
from api.deep_link import *
from api.bot_commands import *
from api.bot_non_commands import *
from api.bot_scdl import *
from api.bot_error import *

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

# Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        STAGE1: [MessageHandler(Filters.regex('^(/start|/queue|/cancel)$'), stage1)],
        STAGE3: [
            MessageHandler(Filters.location, stage3),
            CommandHandler('skip', stage3),
        ],
        STAGE4: [MessageHandler(Filters.text & ~Filters.command, stage4)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

# on different commands - answer in Telegram
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("queue", queue))
dp.add_handler(CommandHandler("queue_mix", queue_mix))
dp.add_handler(CommandHandler("add", add))
dp.add_handler(CommandHandler("sub", sub))
dp.add_handler(CommandHandler("scdl", scdl_command))
dp.add_handler(CommandHandler("update", run_update))

dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(CommandHandler("bad_command", bad_command))

# on noncommand i.e message - echo the message on Telegram
dp.add_handler(InlineQueryHandler(inlinequery))
dp.add_handler(
    MessageHandler(
        Filters.text & ~Filters.command,
        search,
    )
)

dp.add_handler(CallbackQueryHandler(search_buttons))
dp.add_handler(conv_handler)
dp.add_error_handler(error_handler)
