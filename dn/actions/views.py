from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from actions.models import resources
# Create your views here.

class ResourceCreateView(CreateView):
    model = resources
    fields = ['resource']
    template_name = "actions/resource_form.html"
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)

@login_required
def resourceDelete(request, **kwargs):
    try:
        item = resources.objects.get(pk=kwargs['r_id'])
        item.delete()
    except Exception:
        item = None
    return HttpResponse("")

def resourceList(request, pk):
    user=User.objects.get(username=pk)
    return resources.objects.filter(user=user)