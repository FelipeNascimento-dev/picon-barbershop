from django.urls import path
from .views import index, detalhe_barbeiro

app_name = 'barbershop'

urlpatterns = [
    path('', index, name='index'),
    path('barbeiro/<str:nome>/', detalhe_barbeiro, name='detalhe_barbeiro'),
]