from django.core.management.base import BaseCommand
from app.models import User

class Command(BaseCommand):

    def _create_users(self):
        users_to_create = [
            User(
                username=f"user #{i}",
                first_name=f"name {i}",
                last_name=f"lastname {i}", 
                password=f"{i}a{i // 10}Mty{i // 100}Q",
                email=f"email_of_user{i}@mail.com"
            ) for i in range(1, 11001)
        ]
        User.objects.bulk_create(users_to_create)
    
    def handle(self, *args,  **options):
        self._create_users()
