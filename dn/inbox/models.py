from django.db import models
from django.conf import settings
from users.models import Team

# Create your models here.
BROADCAST_TYPE_CHOICES = (
    ("notificatioin", "notificatioin"),
    ("email", "email"),
)
from django.db import models
from django.conf import settings

BROADCAST_TYPE_CHOICES = [
    ('notification', 'Notification'),
    ('email', 'Email'),
]


class Messages(models.Model):
    message = models.TextField()
    broadcaster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="broadcaster")
    type = models.CharField(
        max_length=20,
        choices=BROADCAST_TYPE_CHOICES,
        default='notification',
    )
    teams = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = "message"
        verbose_name = "message"

    def __str__(self):
        return f"{self.broadcaster} ({self.type})"

