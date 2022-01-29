from django.db import models

class List(models.Model):
    name = models.CharField(max_length=100)
    # items = models.ManyToManyField(Item)

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
