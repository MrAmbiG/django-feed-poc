from allauth.account.signals import user_logged_in, user_signed_up, user_logged_out
from notifications.signals import notify
from django.dispatch import receiver
from django.utils import timezone



@receiver(user_logged_in)
def userLogin_handler(request, user, **kwargs):
    notify.send(user, recipient=user, verb='you logged in')


@receiver(user_signed_up)
def userSignup_handler(request, user, **kwargs):
    notify.send(user, recipient=user, verb='you signed up')

@receiver(user_logged_out)
def userLogout_handler(request, user, **kwargs):
    notify.send(user, recipient=user, verb='you logged out')
