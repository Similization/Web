from django.core.management.base import BaseCommand
from app.models import LikesForAnswer, Profile, Answer
from random import choice

class Command(BaseCommand):

    def _create_likes4answer(self):

        answer_ids = Answer.objects.values_list('id', flat=True)
        author_ids = Profile.objects.values_list('id', flat=True)

        likes4answer_to_create = [
            LikesForAnswer(
                likes=1 if i % 3 != 0 else -1, 
                author_id=i // 100 + 1,
                answer_id=i % 10000 + 1
            ) for i in range(1000000)
        ]
        LikesForAnswer.objects.bulk_create(likes4answer_to_create, batch_size=100000)
    
    def handle(self, *args,  **options):
        self._create_likes4answer()
