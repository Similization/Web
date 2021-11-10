from django.core.management.base import BaseCommand
from app.models import LikesForQuestion, Profile, Question
from random import choice

class Command(BaseCommand):

    def _create_likes4question(self):

        question_ids = Question.objects.values_list('id', flat=True)
        author_ids = Profile.objects.values_list('id', flat=True)

        likes4question_to_create = [
            LikesForQuestion(
                likes=1 if i % 3 != 0 else -1, 
                author_id=i // 200 + 1,
                question_id=i % 110000 + 1
            ) for i in range(2000000)
        ]
        LikesForQuestion.objects.bulk_create(likes4question_to_create, batch_size=100000)
    
    def handle(self, *args,  **options):
        self._create_likes4question()
