from django.core.management.base import BaseCommand
from example import views

class Command(BaseCommand):
    help = ""
    def handle(self, *args, **options):
        print("=== start ======")
        
        views.getDataAccount()
        
        print("=== end process")