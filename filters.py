import re

from config import GOOD_DOMAINS, BAD_WORDS, MESSAGE_SEND_FREQUENCY
from db_writer import DataWriter


db_info = DataWriter()


regex = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}'


async def filter_text(message: str, user_tg_id: int, timestamp: float):
    # check spam
    msg_and_time = db_info.get_user_msg(user_tg_id)
    msg = msg_and_time[0][0]
    time = msg_and_time[0][1]
    sec = timestamp - time
    if sec <= MESSAGE_SEND_FREQUENCY or message.lower() == msg:
        return True

    # urls filter
    domains = re.findall(regex, message.lower())
    if GOOD_DOMAINS:
        if domains:
            for domain in GOOD_DOMAINS:
                if domain in domains:
                    domains.remove(domain)
            if domains != []:
                return True

    # bad words filter
    for word in BAD_WORDS:
        if word.lower() in message.lower():
            return True

