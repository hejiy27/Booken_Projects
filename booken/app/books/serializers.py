from rest_framework import serializers

from books.models import Author,Publisher,Book

class SerializerAuthor(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class SerializerPublisher(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name']

class SerializerBook(serializers.ModelSerializer):
    author = SerializerAuthor()
    publisher = SerializerPublisher()
    class Meta:
        model = Book
        fields =[
            'name',
            'isbn',
            'cover_image_url',
            'weight',
            'page',
            'sale_price',
            'grade',
            'author',
            'publisher',
        ]