# crud_project/myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import MyModel
from django.core.serializers import serialize
import json

def index(request):
    my_objects = MyModel.objects.all()
    json_data = serialize('json', my_objects)
    data = json.loads(json_data)
    return JsonResponse(data, safe=False)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        print(name,description)
        MyModel.objects.create(name=name, description=description)
        return redirect('index')
    else:
        print('i am creator')
        return render(request, 'myapp/create.html')

def update(request, pk):
    my_object = get_object_or_404(MyModel, pk=pk)
    if request.method == 'POST':
        my_object.name = request.POST.get('name')
        my_object.description = request.POST.get('description')
        my_object.save()
        return redirect('index')
    else:
        return render(request, 'myapp/update.html', {'my_object': my_object})

def delete(request, pk):
    my_object = get_object_or_404(MyModel, pk=pk)
    my_object.delete()
    return redirect('index')

def api_data(request):
    data = list(MyModel.objects.all().values())
    return JsonResponse(data, safe=False)
