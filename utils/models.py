from django.db import models
from datetime import datetime

# Create your models here.

class CreateUpdate(models.Model):
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = datetime.now()
        
        self.updated_date = datetime.now()
        super().save(*args, **kwargs)
        
    class Meta:
        abstract = True
        
