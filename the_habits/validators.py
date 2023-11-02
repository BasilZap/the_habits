from rest_framework.serializers import ValidationError


class RewardAndRelatedValidator:
    def __init__(self, reward, related):
        self.reward = reward
        self.related = related

    def __call__(self, values):
        reward = dict(values).get(self.reward)
        related = dict(values).get(self.related)
        if reward and related:
            raise ValidationError('Необходимо выбрать только вознаграждение или связанную привычку')


class TimeToCompleteValidator:

    def __init__(self, duration):
        self.duration = duration

    def __call__(self, values):
        duration = dict(values).get(self.duration)
        if duration > 120:
            raise ValidationError('Время выполнения не должно превышать 120 секунд')


class RelatedPleasantValidator:

    def __init__(self, pleasant):
        self.pleasant = pleasant

    def __call__(self, values):
        habit = dict(values).get(self.pleasant)
        if habit:
            if not habit.pleasant_sign:
                raise ValidationError('Связанная привычка должна быть приятной')


class PleasantHabitValidator:
    def __init__(self, pleasant, reward, related):
        self.reward = reward
        self.related = related
        self.pleasant = pleasant

    def __call__(self, values):
        reward = dict(values).get(self.reward)
        related = dict(values).get(self.related)
        pleasant = dict(values).get(self.pleasant)

        if pleasant and reward:
            raise ValidationError('У приятной привычки не может быть вознаграждения')
        if pleasant and related:
            raise ValidationError('У приятной привычки не может быть связанной привычки')


class HabitFrequencyValidator:

    def __init__(self, frequency, pleasant_sign):
        self.frequency = frequency
        self.pleasant_sign = pleasant_sign

    def __call__(self, values):
        frequency = dict(values).get(self.frequency)
        pleasant_sign = dict(values).get(self.pleasant_sign)
        if not pleasant_sign:
            if frequency > 7:
                raise ValidationError('Привычка должна выполняться не менее одного раза в неделю!')
