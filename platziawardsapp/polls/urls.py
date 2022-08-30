# Django
from django.urls import path
# Views
from . import views

app_name = "polls"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('poll/<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('poll/<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('poll/<int:question_id>/vote/', views.vote, name='vote'),
]