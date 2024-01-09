from django.test import TestCase
from client import models


class ModelTest(TestCase):

    def test_tag_model_str(self):
        user = models.User.objects.create(
            name="NameUser",
            game="Need to play"
        )

        self.assertEqual(str(user), user.task_name)