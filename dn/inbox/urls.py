from django.urls import path, include, re_path
import notifications.urls
from inbox import views

urlpatterns = [
    re_path('^notifications/', include(notifications.urls, namespace='notifications')),
    path("notices/", views.getNotifications, name="notificiations_view"),
    path("notice/<int:n_id>/read/", views.notification_read, name="notification_read"),
    path('notice/count/', views.notificationCount, name='notification_count'),
]