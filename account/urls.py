from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [

    path("signin/", views.signin, name="signin"),
    path("login/", views.login, name="login"),
    path("jobber/signup/", views.jobber_signup, name="jobber_signup"),
    path("jobber/createaccount", views.create_jobber_account, name="create_jobber"),
    path("customer/signup/", views.customer_signup, name="customer_signup"),
    path("customer/createaccount", views.create_customer_account, name="create_customer"),
    path("profile/", views.profileView, name="profile_view"),
    path("logout/", views.logout, name="logout")
]