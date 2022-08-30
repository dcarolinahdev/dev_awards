# Django
from django.contrib import admin
# Models
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    """
    **Choices in Questions**

    This admin class is a design for choice inline in questions admin site.

    Model: **Choice**

    Extra attributes:

    - **extra**: 1 -> One space for add a choice for a question
    """
    model = Choice
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    **Questions**

    This admin class is a design for questions in django admin site.

    Model: **Question**

    Extra attributes:

    - fields
    - inlines
    - list_display
    - list_filter
    - search_fields
    """
    fields = ['pub_date', 'question_text']
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
