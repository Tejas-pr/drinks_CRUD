from rest_framework import serializers
from .models import Drink, Nutrition

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'

class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrition
        fields = '__all__'