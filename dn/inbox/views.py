from django.shortcuts import render
from notifications.models import Notification
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse


# Create your views here.
def getNotifications(request, pk):
    user = User.objects.get(username=pk)
    notifications = user.notifications.unread().count()
    context = {'notifications': notifications}
    print(context)
    return render(request, "notifications.html", context)


def notificationCount(request, pk):
    try:
        user = User.objects.get(pk=pk)
        count = user.notifications.unread().count()
    except Exception:
        count = 0
    print(count)
    return JsonResponse({"count": count})


@login_required
def notification_read(request, pk, n_id):
    notice = Notification.objects.get(recipient=pk, id=n_id)
    notice.unread = False
    notice.save()
    data = {'success': True}
    return JsonResponse(data)

