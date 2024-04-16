from django.urls import path
from . import views


urlpatterns= [
    path('', views.login_register, name="login"),
    path('estudiante/', views.estudiante, name="estudiante"),
    path('estudiante/curso/<str:cursoid>', views.estudiante_curso, name="estudiante"),
    path('profesor/', views.profesor, name="profesor")
]