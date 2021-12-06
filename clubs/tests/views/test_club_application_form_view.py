from django.test import TestCase
from django.urls import reverse
from clubs.forms import ClubApplicationForm
from clubs.models import User, Club

class ClubApplicationFormViewTestCase(TestCase):
    """Tests the Club Application form View"""

    fixtures = [
        'clubs/tests/fixtures/default_user.json',
        'clubs/tests/fixtures/default_club.json',
    ]

    def setUp(self):
        self.url = reverse('join_club')
        self.form_input = {
            'statement': "Hey, I would love to join the club!"
        }
        self.user = User.objects.get(username='johndoe')
        self.club = Club.objects.get(name='ChessHub')

    def test_club_application_form_url(self):
        self.assertEqual(self.url, '/join_club/')

    def test_get_club_application_form(self):
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
        club_member = ClubMember.objects.get(
            user = 'janedoe',
            club = 'Chessy'
        )
        # self.assertTrue(self.is_logged_in())
