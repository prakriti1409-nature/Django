from celery import shared_task

@shared_task
def send_welcome_email(email):
    print(f"Sending welcome mail to {email}")
