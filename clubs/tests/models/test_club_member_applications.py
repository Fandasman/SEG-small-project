from django.core.exceptions import ValidationError
from django.test import TestCase
from clubs.models import User, Club, ClubMemberApplications

# Create your tests here.
class ClubMemberApplicationsModelTestCase(TestCase):
    """Unit tests of the club member applications model."""

    fixtures = ['clubs/tests/fixtures/default_user.json',
                'clubs/tests/fixtures/default_club.json',
                'clubs/tests/fixtures/default_club_member_applications.json',
                'clubs/tests/fixtures/other_users.json',
                'clubs/tests/fixtures/other_clubs.json',
                'clubs/tests/fixtures/other_club_members_applications.json']

    def setUp(self):
        self.user = User.objects.get(username = 'johndoe')
        self.club = Club.objects.get(name = 'ChessHub')
        self.club_member_applications = ClubMemberApplications.objects.get(
            user = 1,
            club = 1,
            personal_statement = "Hello",
            status = "P"
        )

# Test club member application must be a unique entry.
    def test_club_member_application_must_be_unique(self):
        second_club_member_application = ClubMemberApplications.objects.get(
            user = 3,
            club = 3,
            personal_statement = "I am interested in joing your club.",
            status = "D"
        )
        self.club_member_applications.user = second_club_member_application.user
        self.club_member_applications.club = second_club_member_application.club
        self._assert_club_member_application_is_invalid()

# Test database reaction upon deleting the content of a foreign key.
    def test_club_member_application_table_is_deleted_upon_deleting_the_club_model(self):
        self.club.delete()
        with self.assertRaises(ClubMemberApplications.DoesNotExist):
            ClubMemberApplications.objects.get(pk = self.club_member_applications.pk)
        self._assert_club_member_application_is_invalid()

    def test_club_member_application_table_is_deleted_upon_deleting_the_user_model(self):
        self.user.delete()
        with self.assertRaises(ClubMemberApplications.DoesNotExist):
            ClubMemberApplications.objects.get(pk = self.club_member_applications.pk)
        self._assert_club_member_application_is_invalid()

# Test case assertions
    def _assert_club_member_application_is_valid(self):
        try:
            self.club_member_applications.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid')

    def _assert_club_member_application_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.club_member_applications.full_clean()