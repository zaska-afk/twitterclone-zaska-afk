from tweeter.models import TwitterUser
from django.shortcuts import render
from .models import Notification


def notification_view(request, id):
    html = 'notifications.html'
    notification = TwitterUser.objects.get(id=id)
    notif = Notification.objects.filter(reciever=notification).filter(seen=False) 

    for item in notif:
        item.seen = True
        item.save()
    
    return render(request, html, {'notification': notification, 'notif': notif})