from django.http import JsonResponse, HttpResponse
from .models import DogBreed



def getDogBreed(request):
    if request.method == 'GET':
        breeds = DogBreed.objects.all().values()

    return JsonResponse(list(breeds),safe=False)

def cronjob(request):
    if request.method == 'GET':
        pass
    return HttpResponse()
