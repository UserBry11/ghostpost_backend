from ghostpost.models import BoastRoast
from rest_framework import serializers


class BoastRoastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoastRoast
        fields = [
            'id',
            'url',
            'title',
            'boolean',
            'content',
            'upvotes',
            'downvotes',
            'post_date'
        ]
