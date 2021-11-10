from django.core.management.base import BaseCommand
from app.models import Answer, Profile, Question
from random import choice

class Command(BaseCommand):

    def _create_answers(self):

        question_ids = Question.objects.values_list('id', flat=True)
        author_ids = Profile.objects.values_list('id', flat=True)

        answers_to_create = [
            Answer(
                question_id=choice(question_ids),
                author_id=choice(author_ids),
                text=f"Some text for {i}answer"
            ) for i in range(1, 1001001)
        ]
        Answer.objects.bulk_create(answers_to_create)
    
    def handle(self, *args,  **options):
        self._create_answers()