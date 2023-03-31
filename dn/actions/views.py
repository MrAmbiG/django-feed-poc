from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from actions.models import resource
# Create your views here.
resource=resource

class ResourceCreateView(CreateView):
    model = resource
    fields = ['resource']
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)

@login_required
def resourceDelete(request, pk):
    try:
        item = resource.objects.get(pk=pk)
        item.delete()
    except Exception:
        item = None
    return HttpResponse("")

def resourceList(request, pk):
    user=User.objects.get(username=pk)
    return resource.objects.filter(user=user)