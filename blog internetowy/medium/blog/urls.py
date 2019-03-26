from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("entry-detail/<int:pk>",
         views.EntryDetailView.as_view(), name="entry-detail"),
    path("entry-create/",
         views.EntryCreateView.as_view(), name="entry-create"),
    path("entry-update/<int:pk>", 
         views.EntryUpdateView.as_view(), name="entry-update"),
    path("entry-delete/<int:pk>", 
         views.EntryDeleteView.as_view(), name="entry-delete"),
     
]
