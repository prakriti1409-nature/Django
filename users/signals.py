from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from api.tasks import send_welcome_email

User = get_user_model()

@receiver(post_save, sender=User)
def on_user_created(sender, instance, created, **kwargs):
    if created and instance.email:
        send_welcome_email.delay(instance.email)
