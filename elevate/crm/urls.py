from django.urls import path

from . import views

urlpatterns = [

    path('', views.homepage, name=""),

    path('register/', views.register, name="register"),

    path('my-login/', views.my_login, name="my-login"),

    path('dashboard/', views.dashboard, name="dashboard"),

    path('user-logout/', views.user_logout, name="user-logout"),
    path('totalusers/', views.totalusers, name="totalusers"),
    path('create/', views.create_student, name='create_student'),
    path('apicreate/', views.YourModelAPIView.as_view(), name='yourmodel-api'),
    
]










