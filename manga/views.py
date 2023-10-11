from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Manga, Genre, Reviews
from .service import MangaFilter
from . import serializers


class MangaAPIViewSet(ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = serializers.MangaListSerializer
    pagination_class = PageNumberPagination
    search_fields = ['name', 'genre__name']
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, )
    filterset_class = MangaFilter
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        serializer = serializers.MangaValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data

        manga = Manga.objects.create(
            name=data.get('name'),
            image=data.get('image'),
            synopsis=data.get('synopsis'),
            release=data.get('release'),
            type_manga=data.get('type_manga')
        )
        manga.genre.set(data.get('genres'))
        return Response(data=serializers.MangaListSerializer(manga, many=False).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        try:
            manga = Manga.objects.get(id=kwargs['id'])
        except Manga.DoesNotExist:
            return Response({'error': 'Manga not found!'}, status=status.HTTP_404_NOT_FOUND)

        return Response(data=serializers.MangaDetailSerializer(manga, many=False).data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        try:
            manga = Manga.objects.get(id=kwargs['id'])
        except Manga.DoesNotExist:
            return Response({'error': 'Manga not found!'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.MangaValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = request.data

        manga.name = data.get('name')
        manga.image = data.get('image')
        manga.type_manga = data.get('type_manga')
        manga.release = data.get('release')
        manga.synopsis = data.get('synopsis')
        manga.genre.set(data.get('genre'))

        manga.save()
        return Response(data=serializers.MangaDetailSerializer(manga, many=False).data, status=status.HTTP_200_OK)


class ReviewAPIViewSet(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = serializers.ReviewsListSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        serializer = serializers.ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data

        review = Reviews.objects.create(
            text=data.get('text'),
            manga_id=data.get('manga_id')
        )
        return Response(data=serializers.ReviewsListSerializer(review, many=False).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        try:
            review = Reviews.objects.get(id=kwargs['id'])
        except Reviews.DoesNotExist:
            return Response({'error': 'Review not found!'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data

        review.text = data.get('text')
        review.manga_id = data.get('manga_id')

        review.save()
        return Response(data=serializers.ReviewsListSerializer(review, many=False).data, status=status.HTTP_200_OK)


class GenreAPIViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenresListSerializer
    lookup_field = 'id'

