from django.shortcuts import render
from notifications.models import Notification
from inbox.forms import BroadcastForm
from inbox.models import Messages
from users.models import Team
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse
from django.forms import modelform_factory
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from notifications.signals import notify
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def adminBroadcast(request, team_qs, message):
    try:
        for team in team_qs:
            receivers = team.members.all()
            for receiver in receivers:
                notify.send(request.user, recipient=receiver, verb=message)
    except Exception as e:
        print(e)

@login_required
def staffBroadcast(request, message):
    receivers = User.objects.all()
    for receiver in receivers:
        notify.send(request.user, recipient=receiver, verb=message)


class BroadcastCreateView(CreateView, LoginRequiredMixin):
    model = Messages
    form_class = BroadcastForm
    template_name = "broadcast.html"
    success_url = reverse_lazy("notifications_view")

    def get_success_url(self):
        # Get the object that was just created
        obj = self.object
        return reverse_lazy("notifications_view", kwargs={"pk": self.request.user})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        team_qs = self.request.user.admin_teams.all()
        form.fields['teams'].queryset = team_qs
        return form

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.broadcaster = self.request.user
        message = instance.message
        if self.request.user.is_staff:
            staffBroadcast(self.request, message)
        else:
            team_qs = self.request.user.admin_teams.all()
            adminBroadcast(self.request, team_qs, message)
        instance.save()
        return super().form_valid(form)

def membership(request):
    admin = False
    teams= Team.objects.all()
    user = request.user
    for team in teams:
        admins = team.admins.all()
        if user in admins:
            admin = True
    return admin or user.is_staff

@login_required
def getNotifications(request, pk):
    user = User.objects.get(username=pk)
    notifications = user.notifications.unread()
    broadcaster = membership(request)
    context = {'notifications': notifications, "broadcaster": broadcaster}
    return render(request, "notifications.html", context)

@login_required
def notificationCount(request, pk):
    try:
        user = User.objects.get(pk=pk)
        count = user.notifications.unread().count()
    except Exception:
        count = 0
    return JsonResponse({"count": count})


@login_required
def notification_read(request, pk, n_id):
    notice = Notification.objects.get(recipient=User.objects.get(username=pk), id=n_id)
    notice.unread = False
    notice.save()
    data = {'success': True}
    return JsonResponse(data)

