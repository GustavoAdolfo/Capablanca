from django.db import models
from django.urls import reverse

class List(models.Model):
    name = models.CharField(max_length=100)
    # items = models.ManyToManyField(Item)

    def get_absolute_url(self):
        return reverse("view_list", args=[self.id])
    

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('id',)
        unique_together = ['list', 'text']
