"""The database seeder generating fake data"""
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.hashers import make_password
from faker import Faker
from clubs.models import User, Club, ClubMember

class Command(BaseCommand):
    """The database seeder."""
    PASSWORD = make_password("Password123", hasher='default')

    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        self.clubs = []

        """Generate set users"""
        User.objects.create(
            username = "clubber",
            first_name = "Clubber",
            last_name = "McClubberson",
            email = "clubber@example.com",
            password = Command.PASSWORD,
            experience = 'professional',
            bio = "I am Clubber, the CEO of McClubberson & Son."
        )

        User.objects.create(
            username = "jebker",
            first_name = "Jebediah",
            last_name = "Kerman",
            email = "jeb@example.org",
            password = Command.PASSWORD,
            experience = 'professional',
            bio = "Hi, I'm Jebediah."
        )

        User.objects.create(
            username = "valker",
            first_name = "Valentina",
            last_name = "Kerman",
            email = "val@example.org",
            password = Command.PASSWORD,
            experience = 'professional',
            bio = "Hi, I'm Valentina."
        )

        User.objects.create(
            username = "billieker",
            first_name = "Billie",
            last_name = "Kerman",
            email = "billie@example.org",
            password = Command.PASSWORD,
            experience = 'professional',
            bio = "Hi, I'm Billie."
        )

        """Create the Kerbal Chess Club"""
        Club.objects.create(
            owner = User.objects.get(username = "billieker"),
            name = 'Kerbal Chess Club',
            location = 'London',
            description = 'This is the one and only Kerbal Chess Club.',
        )

        self.clubs.append(Club.objects.get(name = 'Kerbal Chess Club'))

        ClubMember.objects.create(
            user = User.objects.get(username = "jebker"),
            club = Club.objects.get(name = 'Kerbal Chess Club'),
            role = 'MEM'
        )

        ClubMember.objects.create(
            user = User.objects.get(username = "valker"),
            club = Club.objects.get(name = 'Kerbal Chess Club'),
            role = 'OFF'
        )

        ClubMember.objects.create(
            user = User.objects.get(username = "billieker"),
            club = Club.objects.get(name = 'Kerbal Chess Club'),
            role = 'OWN'
        )

        """Generate other set clubs"""
        # Create club one
        self.club = Club.objects.create(
            owner = User.objects.get(username = "clubber"),
            name = 'Chessie Club',
            location = 'London',
            description = 'This is the one and only Chessie Club.',
        )
        self.clubs.append(self.club)

        ClubMember.objects.create(
            user = User.objects.get(username = "jebker"),
            club = self.club,
            role = 'OFF'
        )

        # Create club 2
        self.club = Club.objects.create(
            owner = User.objects.get(username = "valker"),
            name = 'Amy MasterClub',
            location = 'London',
            description = 'This is the one and only Amy MasterClub.',
        )
        self.clubs.append(self.club)

        ClubMember.objects.create(
            user = User.objects.get(username = "valker"),
            club = self.club,
            role = 'OWN'
        )

        # Create club 3
        self.club = Club.objects.create(
            owner = User.objects.get(username = "clubber"),
            name = 'Clubbie Club',
            location = 'London',
            description = 'This is the one and only Clubbie Club.',
        )
        self.clubs.append(self.club)

        ClubMember.objects.create(
            user = User.objects.get(username = "billieker"),
            club = self.club,
            role = 'MEM'
        )

        """Generate six more random fake clubs"""
        for i in range(6):
            fakeName = self.faker.company()
            fakeLocation = self.faker.address()
            fakeDescription = self.faker.text(max_nb_chars = 520)

            self.club = Club.objects.create(
                owner = User.objects.get(username = "clubber"),
                name = fakeName,
                location = fakeLocation,
                description = fakeDescription,
            )

            ClubMember.objects.create(
                user = User.objects.get(username = "clubber"),
                club = self.club,
                role = 'OWN'
            )

            self.clubs.append(self.club)

        n = 0

        """Generate 100 random fake users and club member objects"""
        for i in range(1, 101):
            fakeUsername = self.faker.user_name()
            fakeName = self.faker.first_name()
            fakeLastName = self.faker.last_name()
            fakeEmail = self.faker.ascii_email()
            fakeBio = self.faker.text(max_nb_chars = 520)

            self.user = User.objects.create(
                username = fakeUsername,
                first_name = fakeName,
                last_name = fakeLastName,
                email = fakeEmail,
                password = Command.PASSWORD,
                experience = 'beginner',
                bio = fakeBio
            )

            if(i % 10 == 0):
                ClubMember.objects.create(
                    user = self.user,
                    club = self.clubs[n],
                    role = 'OFF'
                )
                n+=1
            else:
                ClubMember.objects.create(
                    user = self.user,
                    club = self.clubs[n],
                    role = 'MEM'
                )
