from rest_framework import serializers
from habits.models import Habit
from habits.validators import (SimultaneousSelectionValidator,
                               LeadTimeValidator,
                               NiceHabitAssociatedValidator,
                               NiceHabitRewardOrAssocitedValidator,
                               PeriodicityValidator)


class HabitSerializers(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            SimultaneousSelectionValidator(field=fields),
            LeadTimeValidator(field=fields),
            NiceHabitAssociatedValidator(field=fields),
            NiceHabitRewardOrAssocitedValidator(field=fields),
            PeriodicityValidator(field=fields)
        ]