from django.core.management.base import BaseCommand
from app.models import Tag

class Command(BaseCommand):

    def _create_tags(self):
        tags_to_create = [
            Tag(
                name=f"tag #{i}"
            ) for i in range(1, 11001)
        ]
        Tag.objects.bulk_create(tags_to_create)
    
    def handle(self, *args,  **options):
        self._create_tags()
