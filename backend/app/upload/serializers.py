from rest_framework import serializers

from core.models import File


class FileSerializer(serializers.ModelSerializer):
    """Serializer class for file object"""

    class Meta:
        model = File
        fields = "__all__"
