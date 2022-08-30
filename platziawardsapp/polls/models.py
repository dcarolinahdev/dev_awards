# Python
import datetime
# Django
from django.db import models
from django.utils import timezone

class Question(models.Model):
    """
    **Question**

    This model is a design to manage questions.

    Attributes:

    - **question_text**: CharField
    - **pub_date**: DateTimeField

    Class functions:

    - question was published recently or no (maximum one day ago).
    """
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField("Date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= (timezone.now() - datetime.timedelta(days=1))

class Choice(models.Model):
    """
    **Choice**

    This model is a design to manage choices.

    Attributes:

    - **question**: ForeignKey
    - **choice_text**: CharField
    - **votes**: IntegerField

    Class functions:

    -
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
