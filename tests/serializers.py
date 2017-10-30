from __future__ import absolute_import

from rest_framework import serializers

from tests.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('content',)
        model = Article
