from django.test import TestCase
from django.urls import reverse
from clubs.forms import ClubApplicationForm
from clubs.models import User, Club, ClubMember
from clubs.tests.helpers import JoinInClubTester, reverse_with_next

class ClubApplicationFormViewTestCase(TestCase):
    """Tests the Club Application form View"""

    fixtures = [
        'clubs/tests/fixtures/default_user.json',
        'clubs/tests/fixtures/default_club.json',
        'clubs/tests/fixtures/default_club_member.json'
    ]

    def setUp(self):
        self.user = User.objects.get(username='johndoe')
        self.target_club = Club.objects.get(name='ChessHub')
        self.url = reverse('join_club', kwargs={'club_id': self.target_club.id})
        self.form_input = {
            'statement': "Hey, I would love to join the club!"
        }

    def test_club_application_form_url(self):
        self.assertEqual(self.url, f'/club/join/{self.target_club.id}')

    def test_get_club_application_form_with_valid_id(self):
        self.client.login(username=self.user.username, password='Password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'join_club.html')

    def test_get_club_application_form_with_invalid_id(self):
        self.client.login(username=self.user.username, password='Password123')
        url = reverse('show_club', kwargs={'club_id': self.user.id+9999})
        response = self.client.get(url, follow=True)
        response_url = reverse('home')
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(response, 'home.html')

    def test_get_club_application_form(self):
        self.client.login(username=self.user.username, password='Password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'join_club.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, ClubApplicationForm))
        self.assertFalse(form.is_bound)

    # def test_unsuccessful_club_application_form(self):
    #     before_count = ClubMember.objects.count()
    #     self.form_input ['statement'] = 'Hello!'
    #     response = self.client.post(self.url, self.form_input)
    #     after_count = ClubMember.objects.count()
    #     self.assertEqual(after_count, before_count)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'join_club.html')
    #     form = response.context['form']
    #     self.assertTrue(isinstance(form, ClubApplicationForm))
    #     self.assertTrue(form.is_bound)
    #     # self.assertFalse(self.is_logged_in())

    def test_successful_club_application_form(self):
        before_count = ClubMember.objects.count()
        response = self.client.post(self.url, self.form_input, follow = True)
        after_count = ClubMember.objects.count()
        self.assertEqual(after_count, before_count + 1)
        response_url = reverse('show_club')
        self.assertRedirects(response, response_url, status_code = 302, target_status_code = 200)
        self.assertTemplateUsed(response, 'show_club.html')
        user = User.objects.get(username='janedoe')
        target_club = Club.objects.get(name='Chessy')
        self.assertEqual(club_member.user.first_name, 'Jane')
        self.assertEqual(club_member.user.last_name, 'Doe')
        self.assertEqual(club_member.user.email, 'janedoe@example.com')
        self.assertEqual(club_member.user.experience, 'beginner')
        self.assertEqual(club_member.club.name, 'Chessy')
        self.assertEqual(club_member.club.location, 'Plovdiv')
        self.assertTrue(self.is_member_of())
