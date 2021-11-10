from django.core.management.base import BaseCommand
from app.models import Question, Profile, Tag
from random import choice, sample, randint

class Command(BaseCommand):

    def _create_questions(self):

        authors = Profile.objects.values_list('id', flat=True)
        
        questions_to_create = [
            Question(
                author_id=choice(authors),
                name=f"Question name {i}",
                text=f"Some text for {i} question"
            ) for i in range(1, 110001)
        ]

        Question.objects.bulk_create(questions_to_create)

        tags_ids = list(Tag.objects.values_list('id', flat=True))
        questions_ids = Question.objects.values_list('id', flat=True)

        tags_questions_rels = []

        for question_id in questions_ids:
            for tag_id in sample(tags_ids, k=randint(1, 5)):
                tags_questions_rels.append(Question.tags.through(tag_id=tag_id, question_id=question_id))
        Question.tags.through.objects.bulk_create(tags_questions_rels, batch_size=10000)
    
    def handle(self, *args,  **options):
        self._create_questions()
