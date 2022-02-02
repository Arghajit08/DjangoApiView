from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

class StudentAPI(APIView):
    def get(self,request):
        objectsmain=Student.objects.all()
        serializer=StudentSerializer(objectsmain,many=True)
        return Response({'status':200,'message':serializer.data})
    
    def post(self,request):
        data=request.data
        serializer=StudentSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
        serializer.save()
        return Response({'status':200,'message':serializer.data})
    
    def put(self,request):
        try:
            objectsmain=Student.objects.get(id=request.data['id'])
            serializer=StudentSerializer(objectsmain,data=request.data,partial=False)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':200,'message':serializer.errors})
            serializer.save()
            return Response({'status':200,'message':serializer.data})
        
        except Exception as ex:
            print(ex)
            return Response({'status':200,'message':'invalid id'})
    
    def patch(self,request):
        try:
            objectsmain=Student.objects.get(id=request.data['id'])
            serializer=StudentSerializer(objectsmain,data=request.data,partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':200,'message':serializer.errors})
            serializer.save()
            return Response({'status':200,'message':serializer.data})
        
        except Exception as ex:
            print(ex)
            return Response({'status':200,'message':'invalid id'})
    
    def delete(self,request):
        try:
            id=request.GET.get('id')
            objectsmain=Student.objects.get(id=id)
            objectsmain.delete()
            return Response({'status':200,'message':'deleted'})
        
        except Exception as ex:
            print(ex)
            return Response({'status':200,'message':'invalid id'})
    
        
        
        

@api_view(['GET'])
def home(request):
     objectsmain=Student.objects.all()
     serializer=StudentSerializer(objectsmain,many=True)
    
     return Response({'status':200,'message':serializer.data})

# @api_view(['POST'])
# def postwork(request):
#     data=request.data
#     serializer=StudentSerializer(data=request.data)
#     if not serializer.is_valid():
#         print(serializer.errors)
    
#     return Response({'status':200,'message':serializer.data})
