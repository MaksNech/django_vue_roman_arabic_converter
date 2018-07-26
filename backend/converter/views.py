from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .convert_classes import convert


@csrf_exempt
def convertation(request):
    if request.method == 'POST':
        try:
            num_value = request.POST['num_value']
            if request.POST['label'] == 'Arabic':
                convertedValue = convert(int(num_value))
            elif request.POST['label'] == 'Roman':
                convertedValue = convert(num_value)
        except Exception as err:
            return err

    return JsonResponse({
        "num_value": convertedValue,
    })
