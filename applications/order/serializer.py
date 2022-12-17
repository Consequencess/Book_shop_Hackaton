from rest_framework import serializers

from applications.books.models import Books
from applications.order.tasks import send_confirm_link
from applications.order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Order
        exclude = ['confirm_code']

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        order.create_confirm_code()
        order.save()
        send_confirm_link.delay(order.user.email, order.confirm_code)
        return order

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        book = Books.objects.get(id=rep['book']).title
        rep['book'] = book
        return rep