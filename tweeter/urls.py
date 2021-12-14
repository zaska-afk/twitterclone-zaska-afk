from django.urls import path
from tweeter import views

urlpatterns = [
    path('user/<int:id>/', views.UserView, name='user'),
    path('follow/<int:id>/', views.follow_view, name='follow'),
    path('unfollow/<int:id>/', views.unfollow_view, name='unfollow'),
]
