from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def simpleResponse(request):
    if request.method == 'GET':
            return Response({"response":"Hello to this simple endpoint!"},status=status.HTTP_200_OK) 