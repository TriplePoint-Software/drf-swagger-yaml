from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas

from drf_swagger_yaml.renderer import SwaggerRenderer


@api_view()
@renderer_classes([SwaggerRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='DRF Swagger YAML')
    schema = generator.get_schema(request)
    return response.Response(schema)
