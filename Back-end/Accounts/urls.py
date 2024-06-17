from django.urls import path
from . import views
from .views import LoginView ,SignupView

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.user_login, name="login"),
    path("signup/", views.user_signup, name="signup"),
    path("logout/", views.user_logout, name="logout"),
    path("check/", views.check_lawyer, name="check"),
    path("change-password/", views.change_password, name="change_password"),
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/signup/', SignupView.as_view(), name='signup'),
]
