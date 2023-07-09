from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Fan
from .serializers import FanSerializer


class FanViewSet(viewsets.ModelViewSet):
    queryset = Fan.objects.all()
    serializer_class = FanSerializer

    @action(detail=True, methods=['post', 'get'])
    def toggle_direction(self, request, pk=None):
        fan = self.get_object()
        fan.direction_next()
        serializer = self.get_serializer(fan)
        return Response(serializer.data)

    @action(detail=True, methods=['post', 'get'])
    def cycle_speed(self, request, pk=None):
        fan = self.get_object()
        fan.speed_next()
        serializer = self.get_serializer(fan)
        return Response(serializer.data)
