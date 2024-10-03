from django.shortcuts import HttpResponse, render, get_object_or_404
from django.template import loader
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-publication_date")[:5]
    context = {"latest_question_list" : latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html" , {"question" : question})

def results(request, question_id):
    response = "Result for question :  %s. "
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting for question %s. " % question_id)