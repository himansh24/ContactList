from django.urls import path
from .views import ContactView,DetailView


urlpatterns=[

    path('',ContactView.as_view()),
    path('<int:id>',DetailView.as_view())


]


