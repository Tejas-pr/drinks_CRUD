from .models import Drink
from .serializers import DrinkSerializer
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
        
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    try:
        # here ill get the id of the drink
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response({
            "data": serializer.data
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