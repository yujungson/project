import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations import models as reservation_models
from users import models as user_models
from restaurants import models as restaurant_models


class Command(BaseCommand):

    help = "This command creates many reservations"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many reservations do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        restaurants = restaurant_models.Restaurant.objects.all()
        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "guest": lambda x: random.choice(users),
                "restaurant": lambda x: random.choice(restaurants),
                "date": lambda x: datetime.now(),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reservations created!"))
