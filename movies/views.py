from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': f'Filme - {instance.title} - excluído com sucesso'},
            status=status.HTTP_204_NO_CONTENT
        )
