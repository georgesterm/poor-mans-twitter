from django.urls import path

from tweet.views import MessagesView, TweetView

app_name = "tweet"
urlpatterns = [
  path("", TweetView.as_view(), name="index"),
  path("api/messages/", MessagesView.as_view(), name="messages")
]