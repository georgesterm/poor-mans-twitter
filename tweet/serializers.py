from email import message
from pyexpat import model
from rest_framework import serializers
from .models import Messages

class MessageSerializer(serializers.ModelSerializer):
  writter = serializers.CharField()
  message = serializers.CharField()
  created_at = serializers.DateTimeField(read_only=True)

  class Meta:
    model = Messages
    fields = [
      'id',
      'writter',
      'message',
      'created_at'
    ]