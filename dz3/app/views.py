from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Profile, Question, Answer, Tag

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

def paginate(objects, request, per_page = 10):
    paginator = Paginator(objects, per_page)
    page = request.GET.get('page')
    return paginator.get_page(page)


def settings(request):
    return render(request, 'settings.html', {})


def index(request):
    num_questions = Question.objects.all().count()
    num_profiles = Profile.objects.all().count()
    num_answers = Answer.objects.all().count()
    num_tags = Tag.objects.all().count() 
    content = {
        'num_questions' : num_questions,
        'num_profiles' : num_profiles,
        'num_answers' : num_answers,
        'num_tags'  : num_tags 
    }
    return render(request, 'index.html', context=content)


def hot(request):
    content = paginate(questions, request, 5)
    return render(request, 'hot.html', {'questions': content})


def new(request):
    content = paginate(questions, request, 5)
    return render(request, 'hot.html', {'questions': content})


def tag(request):
    content = paginate(questions, request, 5)
    return render(request, 'tag.html', {'questions': content})


def question(request):
    return render(request, 'question.html', {'questions': qa})


def login(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'register.html', {})


def ask(request):
    return render(request, 'ask.html', {})
