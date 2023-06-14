from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register_user"),
    path('accounts/login/', auth_views.LoginView.as_view(
            template_name='authenticate/login.html',
        )),
  
]
