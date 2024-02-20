from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from .models import order
from django.core.serializers import serialize
from django.http import JsonResponse
import json

def my_view(request):
    data=order.objects.all()

    #order.objects.create(item='mine',place='bengaluru',price=100,paytype='cash')
    json_data = serialize('json', data)
    data1 = json.loads(json_data)
    return JsonResponse(data1, safe=False)
    if request.method == 'POST':
        data={'item':'shankar', 'price':100, 'place':'bengaluru', 'paytype':'cash'}
        order.item='mine'
        order.place='bengaluru'
        order.price=100
        order.paytype='cash'

    else:
        return HttpResponse('my_template.html')