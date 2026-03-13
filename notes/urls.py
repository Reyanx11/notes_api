from django.urls import path
from notes import views

urlpatterns =[
    path('notes/',views.note_list,name = "note_list"),
    path('notes/<int:pk>/',views.note_details,name = "note_details"),
]

