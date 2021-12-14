from tweeter.models import TwitterUser
from notification.models import Notification
from django.shortcuts import render, reverse, HttpResponseRedirect
from tweet.models import Tweet
from tweet.forms import AddTweetForm
from django.contrib.auth.decorators import login_required
import re

def tweet_view(request, id: str):
    tweet = Tweet.objects.get(id=id)
    return render(request, 'tweet.html', {'tweet': tweet, })


@login_required
def AddTweet(request):
    notifications = Tweet.objects.filter(author=request.user)
    if request.method == 'POST':
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                author=request.user,
                body=data['body']
            )
            if '@' in data['body']:
                mentions = re.findall(r'@(\w+)', data['body'])
                recipients = mentions[0]
                recipient_username = TwitterUser.objects.get(username=recipients)

                Notification.objects.create(
                    reciever=recipient_username,
                    tweet=tweet,
                )
        return HttpResponseRedirect(reverse('home'))
    form = AddTweetForm
    return render(request, "generic_form.html", {"form": form, 'notification': notifications})

