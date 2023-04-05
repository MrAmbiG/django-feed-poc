from allauth.account.signals import user_logged_in, user_signed_up, user_logged_out
from inbox import signals
from notifications.signals import notify
from django.dispatch import receiver
from django.utils import timezone
from users.models import Team

@receiver(user_logged_in)
def userLogin_handler(request, user, **kwargs):
    notify.send(user, recipient=user, verb='you logged in')


@receiver(user_signed_up)
def userSignup_handler(request, user, **kwargs):
    notify.send(user, recipient=user, verb='you signed up')

@receiver(user_logged_out)
def userLogout_handler(request, user, **kwargs):
    notify.send(user, recipient=user, verb='you logged out')

@receiver(signals.resourceAddSignal)
def resourceAdd_handler(sender, resource, **kwargs):
    # sender = User.objects.get(pk=sender.user.id)
    notify.send(sender, recipient=sender, verb=f'{resource} added')
    try:
        teams = Team.objects.filter(members=sender)
        for team in teams:
            admins = team.admins.all()
        for admin in admins:
            notify.send(sender, recipient=admin, verb=f'{sender} added {resource}')
    except Exception as e:
        print(e)

@receiver(signals.resourceDeleteSignal)
def resourceDelete_handler(sender, resource, **kwargs):
    # sender = User.objects.get(username=sender)
    notify.send(sender, recipient=sender, verb=f'{resource} deleted')
    try:
        teams = Team.objects.filter(members=sender)
        for team in teams:
            admins = team.admins.all()
        for admin in admins:
            notify.send(sender, recipient=admin, verb=f'{sender} deleted {resource}')
    except Exception as e:
        print(e)
