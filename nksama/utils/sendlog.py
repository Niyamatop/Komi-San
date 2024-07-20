from nksama import bot


def send_log(err, module):
    bot.send_message(-1002239117016, f"error in {module}\n\n{err}")
