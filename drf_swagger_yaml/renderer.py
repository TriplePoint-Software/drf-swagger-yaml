from rest_framework import renderers

from drf_swagger_yaml.codec import OpenAPICodec


class SwaggerRenderer(renderers.BaseRenderer):
    media_type = 'application/openapi+yaml'
    format = 'swagger'

    def render(self, data, media_type=None, renderer_context=None):
        codec = OpenAPICodec()
        return codec.dump(data)
