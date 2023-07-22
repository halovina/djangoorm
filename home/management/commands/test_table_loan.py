from typing import Any, Optional
from django.core.management.base import BaseCommand
# from home.views_crud import createLoan, readAllLoan, updateLoan, deleteLoan
from home import views_filter

class Command(BaseCommand):
    help = ""
    def handle(self, *args, **options):
        print("=== start table loan")
        # views_insert_foreforeginkey.insertTblForeignKey1()
        
        # views_insert_foreforeginkey.insertTblForeignkey2()
        
        views_filter.filterByRange()
        
        print("=== end process")
        
    
        
    