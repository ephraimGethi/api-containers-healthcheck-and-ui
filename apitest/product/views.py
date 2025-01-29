from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import computerSerializer,RoomSerializer
from rest_framework import status
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser,JSONParser
from .models import computer,Rooms
from rest_framework.decorators import api_view
# Create your views here.

class ComputerView(APIView):
    parser_classes = [MultiPartParser,FormParser]
    def post(self,request):
        serializer = computerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors)
    
    def get(self,request):
        qs = computer.objects.all()
        serializer = computerSerializer(qs,many = True)
        return Response(serializer.data)

@api_view(['POST','GET'])
def addNewRooms(request):
    if request.method == 'POST':
        if isinstance(request.data,list):
            serializer = RoomSerializer(data=request.data,many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
        elif isinstance(request.data,dict):
            serializer = RoomSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
             qs = Rooms.objects.all()
             serialializer = RoomSerializer(qs,many=True)
             return Response(serialializer.data)
    
    
