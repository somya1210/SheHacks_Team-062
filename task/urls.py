from django.urls import path
from . import views

urlpatterns=[path("",views.home,name="homepage"),
            path("userform", views.userlogin, name="user"),
            path("registration", views.register, name="register"),
            path("userprofile", views.userprofile, name="userprofile"),
#path("online_events", views.online_events, name="events"),
#path("books", views.books, name="book"),
path("helpline",views.helpline,name="expert"),
path("update/<int:pk>/", views.update, name="update"),
path("day_challenge",views.challenge,name="challenge")
             ]