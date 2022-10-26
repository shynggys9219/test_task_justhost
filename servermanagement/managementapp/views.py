from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


from .models import VPS
from .serializers import VPSSerializer, VPSStatusSerializer

# основная страница со всеми доступными vps
# ip_address:port/ (e.g. localhost:8000/)
@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        'vps list': reverse('vps-list', request=request, format=format)
    })


# общее представление (generics) для vps 
# обрабатывает методы [GET, POST] 
class VPSList(generics.ListCreateAPIView):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer

    # фильтрация по параметрам модели VPS
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = "__all__"
    
    # поиск по колонке
    search_fields = ("^cpu",)

    # только авторизованные пользователи могут получить доступ к небезопасным запросам POST, PUT, [DELETE*]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# generics view для получения данных для конкретного vps
# доступные методы [GET, PUT]
class VPSDetail(generics.RetrieveUpdateAPIView):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer   
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # в задании было сказано, менять только статус у сервера
    # поэтому переопределяю основной serializerна новый только с одним полем status
    def get_serializer_class(self, *args, **kwargs):
        serializer_class = self.serializer_class
        if self.request.method=="PUT":
            serializer_class = VPSStatusSerializer
        return serializer_class
    
