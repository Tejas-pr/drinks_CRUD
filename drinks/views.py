from .models import Drink
from .serializers import DrinkSerializer
from django.http import JsonResponse

def drink_list(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({
        'drinks': serializer.data
    }, safe=False)