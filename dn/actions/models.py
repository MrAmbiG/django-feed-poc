from django.db import models
from django.conf import settings
import uuid



# Create your models here.

class resources(models.Model):
    USER_CHOICES =(
    ("gpu", "gpu"),
    ("vm", "vm"),
    ("baremetal", "baremetal"),
    ("k8s", "k8s"),
)
    resource = models.CharField(max_length=30, choices=USER_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "resources"
        managed = True
        verbose_name = "resources"

    def __str__(self):
        return self.resource


