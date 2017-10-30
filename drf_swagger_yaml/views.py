from rest_framework.response import Response
from rest_framework.views import APIView

from drf_swagger_yaml.api_docs import ApiDocumentation


class DRFSwaggerYamlView(APIView):
    drf_router = None

    def get(self, request, *args, **kwargs):
        docs = ApiDocumentation(drf_router=self.drf_router)
        endpoints = docs.get_endpoints()

        return Response(data='', content_type='text/yml')
