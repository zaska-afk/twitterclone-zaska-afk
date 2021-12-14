from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tweeter.models import TwitterUser

# Register your models here.

class TwitterUserAdmin(UserAdmin):
    
    model = TwitterUser


admin.site.register(TwitterUser, TwitterUserAdmin)
