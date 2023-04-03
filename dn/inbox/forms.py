from django import forms
from django.contrib.auth.models import User
from users.models import Team
from inbox.models import Messages
from django.forms import ModelForm


class BroadcastForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['message', 'type', 'teams']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['teams'].queryset = Team.objects.filter(admins=user)