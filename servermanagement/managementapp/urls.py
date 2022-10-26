from django.urls import path
from django.views.generic import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    # ip_address:port вернет все доступные vps (страница по умолчанию в browsable api)
    path("", api_root, name="api-root"),

    # показать список доступных vps
    path("api/vps/all/", VPSList.as_view(), name="vps-list"),
    
    # показать детали vps по основному ключу в базе (uid)
    path("api/vps/<int:pk>/", VPSDetail.as_view(), name="vps-detail"),
]

# дать выбор между browsable api и обычный json view
# ip_address:port/?format=api (default)
# ip_address:port/?format=json
urlpatterns = format_suffix_patterns(urlpatterns)