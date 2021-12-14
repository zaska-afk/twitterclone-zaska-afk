from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from tweeter.models import TwitterUser
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required

def UserView(request, id):
    html = "user.html"
    user = TwitterUser.objects.get(id=id)
    tweets = Tweet.objects.filter(author=user).order_by('-date')
    return render(request, html, {'user': user, 'tweets': tweets})


@login_required
def follow_view(request, id):
    user = TwitterUser.objects.get(id=id)
    request.user.following.add(user.id)
    user.save()
    return HttpResponseRedirect(reverse('home'))


@login_required
def unfollow_view(request, id):
    user = TwitterUser.objects.get(id=id)
    request.user.following.remove(user.id)
    user.save()
    return HttpResponseRedirect(reverse('home'))