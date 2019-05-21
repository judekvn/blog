from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404

from news.models import Article, Journalist
from news.api.serializer import ArticleSerializer, JournalistSerializer

class JournalistListCreateAPIView(APIView):
    
    def get(self, request):
        journalist = Journalist.objects.all()
        serializer = JournalistSerializer(journalist, many=True, context={'request': request}) #context...?
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleListCreateAPIView(APIView):
    def get(self, request):
        article = Article.objects.filter(active=True)
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class ArticleDetailAPIView(APIView):
    def get_object(self, pk):
        article = get_object_or_404(Article, pk=pk)
        return article
    
    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# @api_view(["GET", "POST"])
# def article_list_create_api_view(request):

#     if request.method == "GET":
#         articles = Article.objects.filter(active=True)
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

# @api_view(["GET", "PUT", "DELETE"])
# def article_detail_api_view(request, pk):

#     try:
#         articles = Article.objects.get(pk = pk)
#     except Article.DoesNotExists:
#         return Response({"error":{
#                 "code": 404,
#                 "message":"Article not found" }
#                 }, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = ArticleSerializer(articles)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         serializer = ArticleSerializer(articles, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)