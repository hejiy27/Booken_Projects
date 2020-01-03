from rest_framework import serializers

from books.models import Author,Publisher,Book

class SnippetSerializerAuthor(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

class SnippetSerializerPublisher(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name']

class SnippetSerializerBook(serializers.ModelSerializer):
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