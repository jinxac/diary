from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Blog
from .serializer import BlogSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class BlogList(APIView):
  permission_classes = [IsAuthenticated|ReadOnly]
  def get(self, request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BlogDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        content = self.get_object(pk)
        serializer = BlogSerializer(content)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        content = self.get_object(pk)
        serializer = BlogSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
