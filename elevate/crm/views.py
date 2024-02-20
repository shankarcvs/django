from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
# - Authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse,HttpResponse
import json
from django.core.serializers import serialize
from .form import StudentForm
from .models import student
from faker import Faker
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class YourModelAPIView(APIView):
    def post(self, request, format=None):
        serializer = StudentForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def generate_create_student(request):
    fake = Faker()
    for _ in range(100):
        name = fake.name()
        mb_no = fake.random_int(min=1000000000, max=9999999999)
        register_no = fake.uuid4()  # Generate a random UUID and take first 15 characters
        email = fake.email()
        pasout = fake.random_int(min=2000, max=2025)

        # Create a new Student object
        student.objects.create(
            name=name,
            mb_no=mb_no,
            register_no=register_no,
            email=email,
            pasout=pasout
        )
    return HttpResponse('success')

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(data=request.data)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse('success')  # Redirect to success page
    else:
        form = StudentForm()
    return render(request, 'crm/create_student.html', {'form': form})
def homepage(request):
    return render(request, 'crm/index.html')

def totalusers(request):
    student.objects.filter(id__lt=4).delete()
    data=student.objects.all()
    json_data = serialize('json', data)
    data1 = json.loads(json_data)
    return JsonResponse(data1, safe=False)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
    context = {'registerform':form}
    return render(request, 'crm/register.html', context=context)
def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")


    context = {'loginform':form}

    return render(request, 'crm/my-login.html', context=context)


def user_logout(request):

    auth.logout(request)

    return redirect("")

@login_required(login_url="my-login")
def dashboard(request):
    return render(request, 'crm/dashboard.html')







