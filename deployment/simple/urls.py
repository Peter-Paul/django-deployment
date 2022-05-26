from django.urls import path
from .views import simpleResponse

urlpatterns = [
    path( '', simpleResponse, name="simple_response" )
]