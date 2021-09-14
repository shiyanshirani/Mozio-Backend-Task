from .models import *
from .serializers import *
from rest_framework import generics
from shapely.geometry import Polygon, Point
from django.http.response import HttpResponse, HttpResponseNotAllowed
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.


class Providerlist(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class Providerdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class PolygonArealist(generics.ListCreateAPIView):
    queryset = PolygonArea.objects.all()
    serializer_class = PolygonAreaSerializer


class PolygonAreadetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PolygonArea.objects.all()
    serializer_class = PolygonAreaSerializer


@api_view(["GET"])
def get_polygon(request):
    """
    Fetching latitude and longitude
    """
    lat = request.GET.get("lat", None)
    long = request.GET.get("long", None)

    if lat is None or long is None:
        return HttpResponse("Invalid lat & long")

    point = Point(float(lat), float(long))
    RESULT_POLYGON = []

    queryset = PolygonArea.objects.all()

    for area in queryset:
        coordinates = area.geojson
        eval_coordinates = eval(coordinates)
        polygon = Polygon(eval_coordinates)
        if polygon.contains(point):
            RESULT_POLYGON.append(area)

    if len(RESULT_POLYGON) == 0:
        return HttpResponse("No service provider registered in the polygon area.")

    serializer = PolygonAreaSerializer(RESULT_POLYGON, many=True)
    return Response(serializer.data)
