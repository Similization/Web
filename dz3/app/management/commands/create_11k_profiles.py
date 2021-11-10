from django.core.management.base import BaseCommand
from app.models import Profile

class Command(BaseCommand):

    def _create_profiles(self):
        profiles_to_create = [
            Profile(
                image=f"/home/danba/Web/dz3/static/img/oblozka.jpg", 
                user_id=i
            ) for i in range(1, 11001)
        ]
        Profile.objects.bulk_create(profiles_to_create)
    
    def handle(self, *args,  **options):
        self._create_profiles()
