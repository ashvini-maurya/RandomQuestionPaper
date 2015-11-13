from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from paper.models import Question, Category


def index(request):
    category_list = Category.objects.all
    category_dic = {'categories': category_list}
    response = render(request, 'index.html', category_dic)
    return response


def about(request):
    return render(request, 'about.html')


def question(request):
    list=[]
    easyQuestions=Question.objects.filter(difficult_level='low').order_by('?')[:10]
    mediumQuestions=Question.objects.filter(difficult_level='medium').order_by('?')[:4]
    list.append(easyQuestions)
    hardQuestions=Question.objects.filter(difficult_level='high').order_by('?')[:4]
    list.append(easyQuestions)
    #getQuestion= getQuestions.order_by('?')[:18]

    return render(request, 'question.html', {'easyQuestions':easyQuestions,'mediumQuestions':mediumQuestions,'hardQuestions':hardQuestions})
