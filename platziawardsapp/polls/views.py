# Django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
# Models
from .models import Question, Choice

"""
def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })

def detail(request, question_id):
    #question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/detail.html", {
        "question": question
    })

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/results.html", {
        "question": question
    })
"""

class IndexView(generic.ListView):
    """
    **Question list**

    This view render a list of questions published until _today_ in descending order of published date.

    Model: **Question**

    Template: **polls/index.html**

    Context:

    - **latest_question_list**: alias for default list.
    """
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five publiched questions"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")

class DetailView(generic.DetailView):
    """
    **Question detailed**

    This view render a detailed question. Only if question was posted.

    Model: **Question**

    Template: **polls/detail.html**
    """
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """Excludes any question that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultView(generic.DetailView):
    """
    **Voting results**

    This view render voting results.

    Model: **Question**

    Template: **polls/results.html**
    """
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    """
    **Vote for a question**

    This view render vote for a question.
    Raise a 404 exception if question is not found.

    Model: **Question**, **Choice**

    Template: **blog/post_list.html**

    Context:

    - **question_id**: question for which results will be printed.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
