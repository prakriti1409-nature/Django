import os, django
from telegram.ext import Updater, CommandHandler
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from users.models import CustomUser

def start(update, context):
    uname = update.message.from_user.username
    if uname:
        user, _ = CustomUser.objects.get_or_create(username=uname)
        user.telegram_username = uname
        user.save()
        update.message.reply_text(f"Hi {uname}! You're registered.")

def run():
    token = config('TELEGRAM_TOKEN')
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    run()
