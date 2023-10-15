from django.test import TestCase, SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_exchange_page_status_code(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)
