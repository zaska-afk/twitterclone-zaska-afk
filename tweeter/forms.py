from tweeter.models import TwitterUser
from django.contrib.auth.forms import UserCreationForm

class TwitterUserCreationForm(UserCreationForm):
    
    class Meta:
        model = TwitterUser
        fields = ('display_name')