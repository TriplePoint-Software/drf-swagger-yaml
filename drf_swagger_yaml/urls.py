from django.conf.urls import url
from drf_swagger_yaml.views import schema_view

urlpatterns = [
    url(r'^$', schema_view, name='drf_swagger_yaml'),
]
