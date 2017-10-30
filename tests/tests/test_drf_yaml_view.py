from django.core.urlresolvers import reverse
from django.test import TestCase


class DRFSwaggerYamlViewTests(TestCase):

    def setUp(self):
        super(DRFSwaggerYamlViewTests, self).setUp()

    def test_model_viewset(self):
        response = self.client.get(reverse('swagger-yaml'))

        self.assertEqual(response.status_code, 200)
