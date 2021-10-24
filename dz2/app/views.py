from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.

questions = [
    {
        "title": f"Title {i}",
        "text": f"Text for {i} question"
    } for i in range(100)
]

qa = [
    {
        "title": f"Title {i}",
        "text": f"{i} answer on question"
    } for i in range(4)
]

def settings(request):
    return render(request, 'settings.html', {})

def index(request):
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'index.html', {'questions': content})

def hot(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'hot.html', {'questions': content})

def tag(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, 'tag.html', {'questions': content})

def question(request):
    return render(request, 'question.html', {'questions': qa})

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'register.html', {})

def ask(request):
    return render(request, 'ask.html', {})
