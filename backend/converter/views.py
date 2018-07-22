from django.shortcuts import render
from .models import Numeral
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import romanify


@csrf_exempt
def convertation(request):
    if request.method == 'POST':
        try:
            num_value = request.POST['num_value']
            if request.POST['label'] == 'Arabic':
                convertedValue = romanify.arabic2roman(num_value)
            elif request.POST['label'] == 'Roman':
                convertedValue = romanify.roman2arabic(num_value)
        except Exception as err:
            return err

    return JsonResponse({
        "num_value": convertedValue,
    })
