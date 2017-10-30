from django.conf.urls import url
from drf_swagger_yaml.views import DRFSwaggerYamlView

urlpatterns = [
    url(r'^$', DRFSwaggerYamlView.as_view(), name='drf_swagger_yaml'),
]
