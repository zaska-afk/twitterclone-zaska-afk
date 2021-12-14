from django.urls import path
from notification import views

urlpatterns = [
    path('notifications/<int:id>/', views.notification_view, name='notifications'),
]