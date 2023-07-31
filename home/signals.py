from django.db.models.signals import pre_init, post_save
from django.dispatch import receiver
from home.models import Event
from datetime import datetime


@receiver(pre_init, sender=Event)
def event_pre_init(sender, **kwargs):
    print("start table event: {}".format(datetime.now()))

@receiver(post_save, sender=Event)
def event_send_email_after_save(sender, **kwargs):
    print("send email to customer start time: {}".format(datetime.now()))