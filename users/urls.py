from django.urls import path
from .views import UserCreation, UserAuth, home_view

urlpatterns = [
    path('login/', UserAuth.as_view(), name='login-user'),
    path('register/', UserCreation.as_view(), name='register-user' ),
    path('', home_view, name='home')

]
