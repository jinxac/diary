from rest_framework import serializers

from mydiary.models import Content

class ContentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Content
    fields = ['id', 'created_at', 'title', 'text']