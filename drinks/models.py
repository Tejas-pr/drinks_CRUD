from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " && " + self.description
    
class Nutrition(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name="nutrition")
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fats = models.FloatField()

    def __str__(self):
        return f"{self.drink.name} Nutrition"
