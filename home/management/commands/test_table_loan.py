from typing import Any, Optional
from django.core.management.base import BaseCommand
# from home.views_crud import createLoan, readAllLoan, updateLoan, deleteLoan
# from home import views_filter
# from home import views_filter_join
# from home import views_filter_group_orderby
# from home import views_query_not
# from home import views_select_only
# from home import views_q_object
# from home import views_subquery
# from home import views_limit_offset
# from home import views_leftjoin_withgroupby
# from home import views_onetoonefield
# from home import views_manytomany
# from home import views_insert_modeluuid
# from home import view_insert_withslug
# from home import views_django_signal
from home import views_viewtotalinvoice


class Command(BaseCommand):
    help = ""
    def handle(self, *args, **options):
        print("=== start ======")
        
        views_viewtotalinvoice.getDataViewTable()
        
        print("=== end process")
        
    
        
    