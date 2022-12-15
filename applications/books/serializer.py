from django.db.models import Avg
from rest_framework import serializers

from applications.books.models import Books, Category


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Books
        fields = '__all__'

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['likes'] = instance.likes.filter(like=True).count()
    #     rep['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']
    #     return rep

    def create(self, validated_data):
        request = self.context.get('request')
        files_data = request.FILES
        post = Books.objects.create(**validated_data)

        # print('POST', post.id, post)
        post.save()


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if not instance.parent:
            rep.pop('parent')
        return rep


