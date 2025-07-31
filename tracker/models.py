from django.db import models

class Expenses(models.Model):
    title = models.CharField(max_length=255)
    amount = models.FloatField()
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title