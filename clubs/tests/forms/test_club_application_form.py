from django.test import TestCase
from django import forms
from clubs.forms import ClubApplicationForm
from clubs.models import User, Club

class ClubApplicationFormTestCase(TestCase):
    """Unit tests of the club application form."""

    def setUp(self):
        self.form_input = {
            'statement': 'Hey, I would like to be a member of this club!',
        }

    def test_valid_club_application_form(self):
        form = ClubApplicationForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_has_necessary_fields(self):
        form = ClubApplicationForm()
        self.assertIn('statement', form.fields)

    def test_form_must_save_correctly(self):
        form = ClubMemberForm(data=self.form_input)
        before_count = ClubMember.objects.count()
        form.save()
        after_count = ClubMember.objects.count()
        self.assertEqual(after_count, before_count + 1)
        club_member = ClubMember.objects.get(
            user = 'janedoe',
            club = 'Chessy'
        )
        self.assertEqual(club_member.user.first_name, 'Jane')
        self.assertEqual(club_member.user.last_name, 'Doe')
        self.assertEqual(club_member.user.email, 'janedoe@example.com')
        self.assertEqual(club_member.user.experience, 'beginner')
        self.assertEqual(club_member.club.name, 'Chessy')
        self.assertEqual(club_member.club.location, 'Plovdiv')