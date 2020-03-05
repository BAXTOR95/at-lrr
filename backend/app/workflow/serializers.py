from rest_framework import serializers

from core.models import Workflow


class WorkflowSerializer(serializers.ModelSerializer):
    """Serializer class for workflow object"""

    class Meta:
        model = Workflow
        fields = "__all__"
