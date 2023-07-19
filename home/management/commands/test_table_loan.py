from typing import Any, Optional
from django.core.management.base import BaseCommand
from home.views_crud import createLoan, readAllLoan, updateLoan, deleteLoan

class Command(BaseCommand):
    help = ""
    def handle(self, *args, **options):
        print("=== start table loan")
        # createLoan()
        # readAllLoan()
        # updateLoan(1)
        deleteLoan(1)
        
        print("=== end process")
        
    