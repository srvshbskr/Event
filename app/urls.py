from django.urls import path
from . import views
urlpatterns = [
    path('',views.homePage,name="home"),
    path('signup',views.signupPage,name="signup"),
    path('login',views.loginPage,name="login"),
    path("logout", views.logoutPage, name= "logout"),
]
