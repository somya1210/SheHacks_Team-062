from django.urls import path
from . import views

urlpatterns=[path("",views.home,name="homepage"),
            path("userform", views.userlogin, name="user"),
            path("registration", views.register, name="register"),
            path("userprofile", views.userprofile, name="userprofile"),
path("MeetTheTeam", views.Team, name="events"),
path("disease", views.disease, name="disease"),
path("helpline",views.helpline,name="expert"),
path("update/<int:pk>/", views.update, name="update"),
path("day_challenge",views.challenge,name="challenge"),
             path("doctor",views.doctor,name="doctor"),
             path("progress",views.progress,name="progress")
             ]