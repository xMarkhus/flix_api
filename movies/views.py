from django.db.models import Count, Avg
from rest_framework import generics, views, status, response
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieListDetailSerializer
from reviews.models import Review
from actors.models import Actor


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer

        return MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer

        return MovieSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response.Response(
            {'message': f'Filme - {instance.title} - excluído com sucesso'},
            status=status.HTTP_204_NO_CONTENT
        )


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genres = self.queryset.values('genre__name').annotate(Count('id'))
        total_reviews = Review.objects.count()
        total_actors = Actor.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(
            data={
                'total_movies': total_movies,
                'movies_by_genre': movies_by_genres,
                'total_reviews': total_reviews,
                'total_actors': total_actors,
                'average_stars': round(average_stars, 1),
            },
            status=status.HTTP_200_OK
        )
