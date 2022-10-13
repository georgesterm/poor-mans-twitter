from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tweet.models import Messages
from tweet.serializers import MessageSerializer

# Create your views here.
class TweetView(TemplateView):
  template_name = "index.html"


class MessagesView(APIView):

  def get(self, request):
    messages = Messages.objects.values()
    return Response({ "messages": messages }, status=status.HTTP_200_OK)
  
  def post(self, request):
    data = request.data
    serializer = MessageSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({ "newMessage": serializer.data}, status=status.HTTP_201_CREATED)