from django.db import models
from django.urls import reverse
from datetime import date

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toy_detail', kwargs={'id': self.id})
    

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    habitat = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    toys = models.ManyToManyField(Toy)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"finch_id": self.id})

    def fed_for_today(self):
        MEALS = (
            ('B', 'Breakfast'),
            ('L', 'Lunch'),
            ('D', 'Dinner')
        )
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    MEALS = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner')
    )
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default='B')
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ('-date',)