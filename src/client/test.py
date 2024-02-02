from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from .models import User, Game


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


class CRUDTestUserGame(APITestCase):
    def setUp(self):
        self.game_data = {"name": "Test Game"}
        self.user_data = {"name": "Test User"}

        self.game = Game.objects.create(**self.game_data)
        self.user_data["games"] = [self.game.id]  # Use list ManyToManyField
        self.user = User.objects.create(**self.user_data)

    def test_create_user(self):
        url = reverse("user-list")
        data = {"name": "New User", "games": [self.game.id]}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 2)

    def test_read_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], self.user.name)
        self.assertEqual(response.data["games"][0]["name"], self.game.name)  # Check if the game is present in the data

    def test_update_user(self):
        url = reverse("user-detail", args=[self.user.id])
        updated_name = "Updated User"
        updated_game_name = "Updated Game"
        data = {"name": updated_name, "games": [self.game.id]}
        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, updated_name)
        self.assertEqual(self.user.games.first().name, updated_game_name)  # Checks to see if the game name has been updated

    def test_delete_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(User.objects.filter(id=self.user.id).exists())

    def test_create_game(self):
        url = reverse("game-list")
        data = {"name": "New Game"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Game.objects.count(), 2)

    def test_read_game(self):
        url = reverse("game-detail", args=[self.game.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], self.game.name)

    def test_update_game(self):
        url = reverse("game-detail", args=[self.game.id])
        updated_name = "Updated Game"
        data = {"name": updated_name}
        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, 200)
        self.game.refresh_from_db()
        self.assertEqual(self.game.name, updated_name)

    def test_delete_game(self):
        url = reverse("game-detail", args=[self.game.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Game.objects.filter(id=self.game.id).exists())