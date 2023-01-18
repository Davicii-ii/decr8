from pyrogram import Client

import os, logging, json

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

##############################################
api_id = 314504
api_hash = "8c64c308e6f0186d495ae1e92a1c228d"
##############################################

decr8 = -1001280481543

try:
    with open(
            "/home/decr8/decr8/res/decr8_data.json",
            "r",
            encoding="utf-8"
    ) as f:
        existing_data = json.load(f)
        with Client("history_update", api_id, api_hash) as app:
            messages = app.get_chat_history(decr8)
            for msg in messages:
                if msg.audio and msg.audio.file_name:
                    if msg.audio.file_name not in existing_data:
                        existing_data[msg.audio.file_name] = msg.id
                        with open(
                                "/home/decr8/decr8/res/decr8_data.json",
                                "w",
                                encoding="utf-8"
                        ) as f:
                            json.dump(existing_data, f)
except FileNotFoundError as e:
    with Client("history_update", api_id, api_hash) as app:
        logging.info(e, "Getting history.")
        d = {
            msg.audio.file_name: msg.id
            for msg in (app.get_chat_history(decr8))
            if msg.audio
            if not None
        }
        logging.info("Done.")
        with open(
                "/home/decr8/decr8/res/decr8_data.json",
                "w",
                encoding="utf-8"
        ) as f:
            logging.info("Writing history to json file.")
            json.dump(d, f)
            logging.info("Done.")
            
os.system("echo lol | sudo -S systemctl restart decr8")
