from rest_framework.response import Response
from rest_framework import status
from books.models import Book
from .serializers import BookSerializer ,UerSeroalizer
from django.http import JsonResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view([ "GET"])
@permission_classes([IsAuthenticated])
def index(request):
    books = Book.objects.all() 
    serializer = BookSerializer( instance=books , many=True)
    return Response(data=serializer.data ,status=status.HTTP_200_OK)

@api_view([ "POST"])
def create(request):
    serializer = BookSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    
        return Response(data={
            "success" : True,
            "message" : "book has been created sucessfuly"
    
        }, status=status.HTTP_201_CREATED)

    return Response(data={
            "success" : False,
            "error" : serializer.errors
    
        }, status=status.HTTP_400_BAD_REQUEST) 


@api_view([ "GET"])
@permission_classes([IsAuthenticated])
def view(request,id):
    books = Book.objects.get(pk=id)
    serializer = BookSerializer( instance=books )
    if serializer:
        return Response(data=serializer.data ,status=status.HTTP_200_OK)
    
    

    return Response(data={
            "success" : False,
            "error" : "not fount "
    
        }, status=status.HTTP_404_NOT_FOUND) 



@api_view([ "PUT"])
def update(request,id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer( book,data = request.data)
    if serializer.is_valid():
        serializer.save()
    
        return Response(data={
            "success" : True,
            "message" : "book has been update sucessfuly"
    
        }, status=status.HTTP_202_ACCEPTED)

    return Response(data={
            "success" : False,
            "error" : serializer.errors
    
        }, status=status.HTTP_400_BAD_REQUEST) 


@api_view(["DELETE"])
def delete(request,id):
    book = Book.objects.get(pk=id)
    book.delete()
    return Response(data={
        "success" : True,
            "message" : "book has been DELETED sucessfuly"
    
        }, status=status.HTTP_200_OK)

    return Response(data={
            "success" : False,
            "message" : "NOT FOUND"
    
        }, status=status.HTTP_400_BAD_REQUEST) 


@api_view(["POST"])
def api_signup(request):
    serializer = UerSeroalizer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    
        return Response(data={
            "success" : True,
            "message" : "user has been registered sucessfuly"
    
        }, status=status.HTTP_201_CREATED)

    return Response(data={
            "success" : False,
            "error" : serializer.errors
    
        }, status=status.HTTP_400_BAD_REQUEST) 









    
    