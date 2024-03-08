from django.urls import path
from .views import TaskCrudAPIView

urlpatterns = [
    path('', TaskCrudAPIView.as_view()),
]