from django.urls import path, include, re_path
from actions.views import ResourceCreateView, resourceDelete

urlpatterns = [
    path("resources/create/", ResourceCreateView.as_view(), name="resource_create"),
    path("resources/delete/<slug:r_id>/", resourceDelete, name="resource_delete"),
]