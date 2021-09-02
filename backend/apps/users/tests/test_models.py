from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_user(email='user@mail.com', password='foo') # noqa

    def test_object_name_is_email(self):
        user = get_user_model().objects.get(user_id=1)
        expected_object_name = user.email
        self.assertEqual(expected_object_name, str(user))
