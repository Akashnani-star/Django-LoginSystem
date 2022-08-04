from django.urls import path
from .views import my_login, my_logout, my_register


urlpatterns = [
    path("register/",my_register,name="my_auth.register"),
    path("login/",my_login,name="my_auth.login"),
    path("logout/",my_logout,name="my_auth.logout"),
]