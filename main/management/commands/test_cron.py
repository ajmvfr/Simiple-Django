from django.core.management.base import BaseCommand
from main.models import Type
from datetime import datetime

class Command(BaseCommand):
    
    help = "generate single record for Cron testing"
    
    def handle(self, *args, **kwargs):

        typeCount = Type.objects.count()
        
        now = datetime.now()
        newTypeNumber = typeCount + 1
        newText = f'type Auto: {newTypeNumber} generated at {now}'
        
        Type.objects.create(name=newText, sort_order=newTypeNumber)
    
    
