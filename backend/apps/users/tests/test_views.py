from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


class LoginViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = get_user_model().objects.create_user(email='user@mail.com', password='foo') # noqa
        self.valid_data = {'email': 'user@mail.com', 'password': 'foo'}
        self.login_url = reverse('login')
        self.signup_url = reverse('sign-up')

    def test_valid_login_returns_status_200(self):
        response = self.client.post(self.login_url, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_response_returns_token(self):
        response = self.client.post(self.login_url, self.valid_data)
        token = response.data['token']
        self.assertIsNotNone(token)

    def test_no_email_password_returns_status_400(self):
        data = {}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_blank_email_password_returns_status_400(self):
        data = {'email': '', 'password': ''}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_credentials_returns_status_404(self):
        data = {'email': 'nonuser@mail.com', 'password': 'foo'}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class SignUpViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = get_user_model().objects.create_user(email='user@mail.com', password='foo') # noqa
        self.existing_data = {'email': 'user@mail.com', 'password': 'foo'}
        self.signup_url = reverse('sign-up')

    def test_sign_up_returns_200(self):
        data = {'email': 'new@user.com', 'password': 'foo'}
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_email_already_exists(self):
        response = self.client.post(self.signup_url, self.existing_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
