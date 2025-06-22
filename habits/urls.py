from habits.apps import HabitsConfig
from django.urls import path

from habits.views import (
    HabitCreateAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("habit/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit-update"),
    path(
        "habit/<int:pk>/destroy/", HabitDestroyAPIView.as_view(), name="habit-destroy"
    ),
    path("habit/", HabitListAPIView.as_view(), name="habit-list"),
    path("habit/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit-retrieve"),
]
