from django.db import models
from django.conf import settings

class Team(models.Model):
    name = models.CharField(max_length=30)
    admins = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="admin_teams")
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="member_teams")

    class Meta:
        ordering = ['name']
        db_table = "team"
        managed = True
        verbose_name = "team"

    def __str__(self):
        return self.name



