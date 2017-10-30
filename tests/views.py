from __future__ import absolute_import

from rest_framework.viewsets import ModelViewSet

from tests.models import Article
from tests.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
