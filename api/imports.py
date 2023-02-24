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

from telegram.utils import (
    helpers
    )

from telegram.error import (
    TelegramError,
    BadRequest
    )

from uuid import uuid4

import random, os, re, json, traceback, logging, html
