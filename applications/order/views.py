from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from applications.order.models import Order
from applications.order.serializer import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        res = queryset.filter(user=user)
        return res

    @action(detail=False, methods=['GET'])
    def order_list(self, request):
        user = request.user
        order_list = user.objects.all()
        serializer = OrderSerializer(order_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderConfirm(APIView):
    @staticmethod
    def get(request, confirm_code):
        try:
            order = Order.objects.get(confirm_code=confirm_code)
            order.order_confirm = True
            order.confirm_code = ''
            order.save()
            return Response({'msg': 'заказ успешно подтвержден'}, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({'msg': 'неправельный код подтверждения заказа'}, status=status.HTTP_400_BAD_REQUEST)
