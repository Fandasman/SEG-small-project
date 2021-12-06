from django.urls import reverse

def reverse_with_next(url_name, next_url):
    url = reverse(url_name)
    url += f"?next={next_url}"
    return url

class LogInTester:
    def is_logged_in(self):
        return '_auth_user_id' in self.client.session.keys()

class JoinInClubTester:
    def is_member_of(self):
        return '_auth_club_member_id' in self.client.session.keys()
