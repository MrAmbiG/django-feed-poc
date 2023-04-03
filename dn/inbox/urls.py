from django.urls import path, include, re_path
import notifications.urls
from inbox import views
from inbox.views import BroadcastCreateView

urlpatterns = [
    re_path('^notifications/', include(notifications.urls, namespace='notifications')),
    path("notices/", views.getNotifications, name="notifications_view"),
    path("notices/<int:n_id>/read/", views.notification_read, name="notification_read"),
    path('notices/count/', views.notificationCount, name='notification_count'),
    # path('notices/broadcast/', views.broadcast, name='broadcast'),
    path('notices/broadcast/', BroadcastCreateView.as_view(), name='broadcast'),
]