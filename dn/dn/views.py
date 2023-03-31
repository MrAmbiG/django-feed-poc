import contextlib
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from config import *
from actions.views import resourceList



def handler404(request, *args, **kwargs):
    return render(request, "404.html", locals())


def handler500(request, *args, **kwargs):
    return render(request, "500.html", locals())


def welcome(request):
    return render(request, "welcome.html")

@login_required
def profile(request):
    return redirect(f"/{request.user.username}")

def rprofile(request, pk):
    context = {
        "pk": pk,
        'resources': resourceList(request, pk)
    }
    return render(request, "profile.html", context)

