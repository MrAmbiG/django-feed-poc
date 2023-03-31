from django.db import models
from django.conf import settings
import uuid



# Create your models here.
# class resource(models.Model):
#     USER_CHOICES =(
#     ("gpu", "gpu"),
#     ("vm", "vm"),
#     ("baremetal", "baremetal"),
#     ("k8s", "k8s"),
# )
#     id = models.UUIDField(
#          primary_key = True,
#          default = uuid.uuid4,
#          editable = False)
#     name = models.CharField(max_length=30, null=False, blank=False)
#     description = models.CharField(max_length=100, null=False, blank=False)
#     resource = models.CharField(max_length=30, choices=USER_CHOICES)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         # db_table = "resource"
#         managed = True
#         # verbose_name = "resource"

#     def __str__(self):
#         return self.resource


class resource(models.Model):
    USER_CHOICES =(
    ("gpu", "gpu"),
    ("vm", "vm"),
    ("baremetal", "baremetal"),
    ("k8s", "k8s"),
)
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    resource = models.CharField(max_length=30, choices=USER_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "resource"
        managed = True
        verbose_name = "resource"

    def __str__(self):
        return self.resource


