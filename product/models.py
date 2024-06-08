from django.db import models

class SavedItem(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    needed_date = models.DateField() 
    created_at = models.DateTimeField(auto_now_add=True)
