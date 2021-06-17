from .models import Poll, Question
from django.contrib import admin


class PersonAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)



admin.site.register(Poll, PersonAdmin)
admin.site.register(Question, QuestionAdmin)
