from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from books.serializers import SerializerBook


class BookListAPIView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = SerializerBook(books, many = True)
        return Response(serializer.data)

