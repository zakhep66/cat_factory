from rest_framework import viewsets

from app.models import Cat
from app.serializers import CatSerializer


class CatVewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def get_queryset(self):
        return Cat.objects.filter(user_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
