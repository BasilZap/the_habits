from django.urls import path, include

from the_habits.apps import TheHabitsConfig
from the_habits.views import HabitCreateAPIView, HabitUpdateAPIView, HabitListAPIView, HabitPublicListAPIView, \
    HabitDestroyAPIView

app_name = TheHabitsConfig.name

urlpatterns = [

    path('create/', HabitCreateAPIView.as_view(), name='create'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update'),
    path('list/', HabitListAPIView.as_view(), name='list'),
    path('public/', HabitPublicListAPIView.as_view(), name='public'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='delete')
]
