from .views import *
from django.urls import path

urlpatterns = [
    path('key/', KeyView.as_view(), name='key'),
    path('', KeyView.as_view(), name='home'),
    path('checkupdate/', UpdateCheck.as_view(), name='update')
]