from rest_framework import generics
from . import models, serializers

# Create your views here.

class PlaceList(generics.ListCreateAPIView):
  serializer_class = serializers.PlaceSerializer

  def get_query(self):
    return models.Place.objects.filter(owner_id=self.request.user.id)

  def perform_create(self, seralizer):
    seralizer.save(owner=self.request.user)