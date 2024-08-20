from django.db import models

class SavedItem(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    needed_date = models.DateField() 
    created_at = models.DateTimeField(auto_now_add=True)


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

