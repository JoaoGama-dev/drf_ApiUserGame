from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from client.models import User, Game

# TODO: Fazer teste completo de CRUD com User e Game
class ClientTest(APITestCase):
    def test_it_lists_users(self):
        # NOTE: Criando modelos para serem listados
        game = Game.objects.create(name="test game")
        User.objects.create(name="test", game=game)

        url = reverse("user-list")
        response = self.client.get(url)
        json = response.json()

        # NOTE: Sempre bom ver se o resultado deu: 200 (listagem), 201 (criação)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json), 1) # Garantindo que o user que criamos foi listado
