from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse 

class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = "admin@xyz.com",
            password = "password123"
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email = "test@xyz.com",
            password = "test123",
            name = "UserFullName"
        )

    def test_users_listed(self):
        # Test that users are listed on userpage
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        # Test that user edit page work
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
    
    def test_create_user_page(self):
        # Test that create user page works
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)