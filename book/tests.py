from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from book.models import Users


class RegisterTestCase(TestCase):
    def test_user_created(self):
        self.client.post(
            reverse("book:register"),
            data={
                "username": "ahmadjon",
                "email": "ahmadjon@gmail.comm",
                "middle_name": "fayzulla o'g'li",
                "first_name": "Ahmadjon",
                "last_name": "Hashimov",
                "password": "testpassword",
                "confirm_password": "testpassword",
                "avatar": SimpleUploadedFile("book/avatar.jpg", "rb")
            }
        )
        user = Users.objects.get(username="ahmadjon")
        self.assertEqual(user.first_name, "Ahmadjon")
        self.assertEqual(user.last_name, "Hashimov")
        self.assertEqual(user.middle_name, "fayzulla o'g'li")
        self.assertNotEqual(user.password, "testpassword")
        self.assertTrue(user.check_password("testpassword"))
        self.assertIsNotNone(user.avatar)

    def test_confirm_password(self):
        response = self.client.post(
            reverse("book:register"),
            data={
                "username": "ahmadjon",
                "email": "ahmadjon@gmail.comm",
                "middle_name": "fayzulla o'g'li",
                "first_name": "Ahmadjon",
                "last_name": "Hashimov",
                "password": "testpassword",
                "confirm_password": "testpassword",
                "avatar": open("book/avatar.jpg", "rb")
            }
        )
        user_count = Users.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('confirm_password', form.errors)
        self.assertEqual(form.errors['confirm_password'], ["password and confirm_password must be match"])
        self.assertEqual(user_count, 0)

    def test_required_fields(self):
        pass

    def test_username_unique(self):
        pass


class LoginTestCase(TestCase):
    def setUp(self):
        self.user = Users.objects.create_user(username="testuser", email="test@gmail.com", password="testpassword")

    def test_login(self):
        #self.user
        pass

    def test_with_empty_params(self):
        #self.user
        pass
