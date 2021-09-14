from django.urls import path
from .views import *

urlpatterns = [
    path("provider/", Providerlist.as_view()),
    path("provider/<int:pk>/", Providerdetail.as_view()),
    path("polygon/", PolygonArealist.as_view()),
    path("polygon/<int:pk>/", PolygonAreadetail.as_view()),
    path("geopolygon/", get_polygon)
]
