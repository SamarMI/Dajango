from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path("",views.index),
    path("create",views.create),
    path("view/<int:id>",views.view),
    path("update/<int:id>",views.update),
    path("delete/<int:id>",views.delete),

    path("login", obtain_auth_token),
    path("signup", views.api_signup)





    




]