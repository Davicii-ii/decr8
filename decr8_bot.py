# -*- coding: utf-8 -*-

import os, sys, json, api

from uuid import uuid4

from api.bot_scdl import *
from api.variables import *
from api.deep_link import *
from api.bot_commands import *
from api.bot_non_commands import *
from api.bot_error import *

#from telegram.utils import (
#    helpers
#    )

def main():
    
    from api import bot_handler
    
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary

    # Start the Bot
    updater.start_polling()
    
    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()    
        
if __name__ == "__main__":
    sys.path.append("/home/decr8/decr8/api")
    main()
    
