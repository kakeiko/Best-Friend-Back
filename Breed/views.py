from django.http import JsonResponse
from .models import DogBreed



def getDogBreed(request):
    if request.method == 'GET':
        breeds = DogBreed.objects.all().values()

    return JsonResponse(list(breeds),safe=False)
