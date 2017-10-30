from __future__ import absolute_import

from django.conf.urls import include, url
from rest_framework.routers import SimpleRouter
from drf_swagger_yaml.views import DRFSwaggerYamlView
from tests import views

router = SimpleRouter()
router.register('article-viewset', views.ArticleViewSet, base_name='article')

urlpatterns = [
    url(r'^swagger-yaml/', DRFSwaggerYamlView.as_view(drf_router=router), name='swagger-yaml'),
    url(r'^', include(router.urls)),
]
