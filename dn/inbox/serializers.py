from rest_framework import serializers
from django.contrib.auth.models import User
from inbox.models import ApiNotify

class NotifyApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiNotify
        fields = ["receiver", "message"]