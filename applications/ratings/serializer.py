from rest_framework import serializers

from applications.ratings.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField()
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating
        fields = ['rating']