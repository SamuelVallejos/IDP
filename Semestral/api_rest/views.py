from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from LineApp.models import Lineup
from .serializers import LineupSerializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@csrf_exempt

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def listado_Lineup(request):
    if request.method == 'GET':
        LineUps = Lineup.objects.all()
        serializer = LineupSerializers(LineUps,many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addLineUp(request):
    data1 = JSONParser().parse(request)
    serializer = LineupSerializers(data = data1)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def controlarLineUp(request,codigo):
    try:
        L = Lineup.objects.get(idLine = codigo)
    except Lineup.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LineupSerializers(L)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = LineupSerializers(L,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        L.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)