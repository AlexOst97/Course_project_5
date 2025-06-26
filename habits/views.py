from rest_framework import generics
from .pagination import MyPageHabitPagination
from .serializers import HabitSerializers
from .models import Habit
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwners


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwners]


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwners]


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    pagination_class = MyPageHabitPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.filter(owner=self.request.user)
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]


class PublishedHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.filter(is_published=True)
    pagination_class = MyPageHabitPagination
    permission_classes = [IsAuthenticated]