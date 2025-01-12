from django.contrib import admin
from .models import Choice, Question, Poll


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    """Poll Admin"""


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    """Choice Admin"""


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Question Admin"""
