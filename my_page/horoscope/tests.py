from http.client import responses

from django.test import TestCase
from . import views

# Create your tests here.

class TetstHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_libra(self):
        response = self.client.get('/horoscope/libra/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)',
                      response.content.decode())

    def test_signs(self):
        for key,value in views.signs.items():
            response = self.client.get(f'/horoscope/{key}/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(value, response.content.decode())

    def test_libra_redirect(self):
        for key, (value, _) in enumerate(views.signs.items(), start=1):
            response = self.client.get(f'/horoscope/{key}/')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{value}/')

