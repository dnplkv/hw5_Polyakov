from account import views
from django.contrib.auth import views as auth_views
from django.urls import path


app_name = 'account'

urlpatterns = [
    path('my-profile/', views.MyProfile.as_view(), name='my_profile'),
    path('my-profile/ava/create/', views.AvaCreate.as_view(), name='my_profile_ava_create'),
    path('my-profile/ava/list/', views.AvaList.as_view(), name='my_profile_ava_list'),
    path('sign-up/', views.SignUpView.as_view(), name='sign_up'),
    path('activate/<str:confirmation_token>', views.ActivateUserView.as_view(), name='activate'),
    path('password/', views.change_password, name='change_password'),
    path('logout/', views.logout, name='user_logout'),
    path('login/', auth_views.LoginView.as_view(template_name="account/user_login.html"), name='user_login'),
]
