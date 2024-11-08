from rest_framework import serializers

from apps.common import models


class VersionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VersionHistory
        fields = ("version", "required")
