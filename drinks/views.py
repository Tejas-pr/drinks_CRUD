from .models import Drink, Nutrition
from .serializers import DrinkSerializer, NutritionSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request, format=None):

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({
            'drinks': serializer.data
        })
    
    if request.method == 'POST':
        data = request.data
        serializer = DrinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'successfull',
                'data_added': serializer.data
            }, status=status.HTTP_201_CREATED)
        
# to add the Nutrition of the drink API

@api_view(['POST'])
def add_nutrition(request, drink_id):
    try:
        drink = Drink.objects.get(id=drink_id)
    except Drink.DoesNotExist:
        return Response({
            "message": "Drink not found"
        }, status=status.HTTP_404_NOT_FOUND)
        
    data = request.data.copy()
    data['drink'] = drink.id
    Nutri_serializer = NutritionSerializer(data=data)
    if Nutri_serializer.is_valid():
        Nutri_serializer.save(drink=drink)
        return Response({
            "message": "Nutrition added successfully",
            "nutrition": Nutri_serializer.data
        }, status=status.HTTP_201_CREATED)
    
    return Response(Nutri_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    try:
        # here ill get the id of the drink
        drink = Drink.objects.get(pk=id)
        nutrition = Nutrition.objects.filter(drink=drink)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        drink_serializer = DrinkSerializer(drink)
        nutrition_data = [
            {"id": nutri.id, "calories": nutri.calories, "protein": nutri.protein, "carbs": nutri.carbs, "fats": nutri.fats}
            for nutri in nutrition
        ]
        return Response({
            "data": drink_serializer.data,
            "nutrition": nutrition_data
        })
    elif request.method == 'PUT':
        data = request.data
        serializer = DrinkSerializer(drink, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "successfull",
                "data": serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)