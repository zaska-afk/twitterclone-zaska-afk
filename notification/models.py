from django.db import models
from tweeter.models import TwitterUser
from tweet.models import Tweet

class Notification(models.Model):
    reciever = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)