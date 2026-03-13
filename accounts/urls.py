from django.urls import path
from .views import userList,UserDetails

urlpatterns =[
    path("user/", userList.as_view()),
    path("user/<int:pk>/", UserDetails.as_view()),
]