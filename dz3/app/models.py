from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Profile(models.Model):
    image = models.ImageField(upload_to="static/img")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'login: ' + self.user.username + ', email: ' + self.user.email


class QuestionManager(models.Manager):
    def new(self):
        return self.filter(date__exact=datetime.date())


    def popular(self):
        return self.filter(rating)


    def tag(self, tag):
        return self.filter(tags__contains=tag)


class Question(models.Model):
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="question")
    tags = models.ManyToManyField(Tag, related_name="questions", blank=True)
    name = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=True)

    objects = QuestionManager()

    def __str__(self):
        return self.name
    

class LikesForQuestion(models.Model):
    LIKE = 1
    DISLIKE = -1
    LIKES_CHOICES = [
        (LIKE, "like"),
        (DISLIKE, "dislike")
    ]

    likes = models.IntegerField(choices=LIKES_CHOICES)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="likes")

    class Meta: 
        unique_together = ('author', 'question')


    def __str__(self):
        return self.author.user.username + " reaction: " + str(self.likes) + "on question: " + self.question.name


    def update_rating():
        question.rating += likes


class Answer(models.Model):
    rating = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="answers")
    text = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=True)


class LikesForAnswer(models.Model):
    LIKE = 1
    DISLIKE = -1
    LIKES_CHOICES = [
        (LIKE, "like"),
        (DISLIKE, "dislike")
    ]

    likes = models.IntegerField(choices=LIKES_CHOICES)
    author = models.OneToOneField(Profile, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        unique_together = ('author', 'answer')

    
    def update_rating():
        answer.rating += likes


    def __str__(self):
        return self.author.user.username + " reaction: " + str(self.likes) + "on answer: " + self.answer.name
