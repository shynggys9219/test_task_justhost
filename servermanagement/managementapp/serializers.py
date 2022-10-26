from rest_framework import serializers
from .models import VPS

# сериалайзер для возврата всех данных о VPS
class VPSSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VPS
        fields= '__all__'


# сериалайзер для PUT метода, чтобы он менял только status сервера
class VPSStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VPS
        fields= ("status",)