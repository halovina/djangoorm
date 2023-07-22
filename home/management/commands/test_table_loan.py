from typing import Any, Optional
from django.core.management.base import BaseCommand
# from home.views_crud import createLoan, readAllLoan, updateLoan, deleteLoan
# from home import views_filter
# from home import views_filter_join
from home import views_filter_group_orderby

class Command(BaseCommand):
    help = ""
    def handle(self, *args, **options):
        print("=== start table loan")
        views_filter_group_orderby.queryGroupBy()
        
        
        
        print("=== end process")
        
    
        
    