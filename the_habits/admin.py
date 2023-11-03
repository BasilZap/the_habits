from django.contrib import admin

from the_habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('action', 'habit_datetime', 'place', 'pleasant_sign', 'frequency', 'related_habit',
                    'reward', 'time_to_complete', 'public_sign', 'owner')
