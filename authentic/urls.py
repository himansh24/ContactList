from django.urls import path
from .views import RegisterView,LoginView

urlpatterns=[
    path('reg/',RegisterView.as_view()),
    path('log/',LoginView.as_view())
]