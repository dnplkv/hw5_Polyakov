from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('my-profile/', views.MyProfile.as_view(), name='my_profile'),
]
