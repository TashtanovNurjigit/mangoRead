from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Manga, Genre, Reviews


class ReviewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class MangaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = 'name image release'.split()


class MangaDetailSerializer(serializers.ModelSerializer):
    reviews_manga = ReviewsListSerializer(many=True)

    class Meta:
        model = Manga
        fields = 'id name image synopsis release type_manga genre reviews_manga'.split()


class MangaValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    type_manga = serializers.CharField(max_length=100)
    synopsis = serializers.CharField()
    release = serializers.IntegerField(min_value=1874, max_value=2023)
    image = serializers.ImageField()
    genres = serializers.ListField()

    def validate_genres(self, genres):
        genre_db = Genre.objects.filter(id__in=genres)
        if len(genre_db) != len(genres):
            raise ValidationError('Genres not found!')
        return genres


class GenresListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewValidateSerializer(serializers.Serializer):
    manga_id = serializers.IntegerField()
    text = serializers.CharField()

    def validate_manga_id(self, manga_id):
        try:
            Manga.objects.get(id=manga_id)
        except Manga.DoesNotExist:
            raise ValidationError(f'Manga with id {manga_id} not found!')
        return manga_id
