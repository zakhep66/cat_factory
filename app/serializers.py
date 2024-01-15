from rest_framework import serializers

from app.models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ["id", "name", "age", "breed", "hairiness"]
        extra_kwargs = {"user_id": {"read_only": True}}
