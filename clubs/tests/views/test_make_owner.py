from django.test import TestCase
from django.contrib.auth.hashers import check_password
from clubs.models import User, Club
from clubs.tests.helpers import LogInTester
from django.urls import reverse
from clubs.tests.helpers import reverse_with_next

class MakeOwnerTest(TestCase):

    fixtures = [
        'clubs/tests/fixtures/default_user.json',
        'clubs/tests/fixtures/other_users.json',
        'clubs/tests/fixtures/default_club.json',
    ]

    def setUp(self):
        self.user = User.objects.get(username='johndoe')
        self.target_user = User.objects.get(username = 'janedoe')
        self.club = Club.objects.get(name = 'ChessHub')
        self.url = reverse('make_owner', kwargs={'club_id': self.club.id})


    def test_password_url(self):
        self.assertEqual(self.url, f'/pass_ownership/{self.club.id}/')

    def test_get_password_redirects_when_not_logged_in(self):
        redirect_url = reverse_with_next('log_in', self.url)
        response = self.client.get(self.url)
        self.assertRedirects(response, redirect_url, status_code=302, target_status_code=200)






