from django.urls import path
from notes import views

urlpatterns =[
    path('notes/',views.NoteList.as_view(),name = "note_list"),
    path('notes/<int:pk>/',views.NoteDetails.as_view(),name = "note_details"),
]

