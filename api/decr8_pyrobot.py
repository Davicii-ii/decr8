from variables import *

with Client("", api_id, api_hash) as app:
    logging.info("Getting history.")
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
    
