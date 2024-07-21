from django.shortcuts import render
from rest_framework.decorators import api_view, APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
# @api_view(['GET'])
# def book_list(request):
#     query = Book.objects.all()
#     serializer = BookSerializer(query, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def book_single_view(request, id):
    query = Book.objects.get(id=id)
    serializer = BookSerializer(query)
    return Response(serializer.data)


@api_view(["POST"])
def logout(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

# @api_view(['POST'])
# def book_post(request):
#     serializer  = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)

# @api_view(['PUT'])
# def book_update(request, id):
#     query = Book.objects.get(id=id)
#     serializer  = BookSerializer(query, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)

# @api_view(['DELETE'])
# def book_delete(request, id):
#     query = Book.objects.get(id=id)
#     query.delete()
#     return Response("Record has been deleted Successfully!!")


class BookView(APIView):
    permission_classes = [IsAuthenticated]
    

    def get(self, request):
        query = Book.objects.all()
        serializer = BookSerializer(query, many=True)
        return Response(serializer.data)
    
    def put(self, request, id):
        query = Book.objects.get(id=id)
        serializer  = BookSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def post(self, request):

        serializer  = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, id):

        query = Book.objects.get(id=id)
        query.delete()
        return Response("Record has been deleted Successfully!!")


    

