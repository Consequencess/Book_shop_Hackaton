from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from . import service
from .serializer import FanSerializer


class LikedMixin:
    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        obj = self.get_object()
        service.add_like(obj, request.user)
        return Response('Лайк успешно поставлен', status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=True)
    def unlike(self, request, pk=None):
        obj = self.get_object()
        service.remove_like(obj, request.user)
        return Response('Лайк успешно убран', status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def fans(self, request, pk=None):
        obj = self.get_object()
        fans = service.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)