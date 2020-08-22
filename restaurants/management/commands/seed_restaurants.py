import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from restaurants import models as restaurant_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates restaurants"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=50,
            type=int,
            help="How many restaurants you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        service_options = restaurant_models.ServiceOptions.objects.all()
        seeder.add_entity(
            restaurant_models.Restaurant,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "service_options": lambda x: random.choice(service_options),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        highlights = restaurant_models.Highlights.objects.all()
        accessibilities = restaurant_models.Accessibility.objects.all()
        offerings = restaurant_models.Offerings.objects.all()
        dining_options = restaurant_models.DiningOptions.objects.all()
        amenities = restaurant_models.Amenities.objects.all()
        atmosphere = restaurant_models.Atmosphere.objects.all()
        crowd = restaurant_models.Crowd.objects.all()
        planning = restaurant_models.Planning.objects.all()
        payments = restaurant_models.Payments.objects.all()

        for pk in created_clean:
            restaurant = restaurant_models.Restaurant.objects.get(pk=pk)
            for i in range(3, random.randint(10, 20)):
                restaurant_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    restaurant=restaurant,
                    file=f"restaurant_photos/{random.randint(1, 31)}.webp",
                )
            for a in highlights:
                magic_number = random.randint(1, 20)
                if magic_number % 2 == 0:
                    restaurant.highlights.add(a)
            for f in accessibilities:
                magic_number = random.randint(1, 5)
                if magic_number % 2 == 0:
                    restaurant.accessibilities.add(f)
            for r in offerings:
                magic_number = random.randint(1, 20)
                if magic_number % 2 == 0:
                    restaurant.offerings.add(r)

            for a in dining_options:
                magic_number = random.randint(1, 20)
                if magic_number % 2 == 0:
                    restaurant.dining_options.add(a)
            for f in amenities:
                magic_number = random.randint(1, 5)
                if magic_number % 2 == 0:
                    restaurant.amenities.add(f)
            for r in atmosphere:
                magic_number = random.randint(1, 20)
                if magic_number % 2 == 0:
                    restaurant.atmosphere.add(r)
            for a in crowd:
                magic_number = random.randint(1, 20)
                if magic_number % 2 == 0:
                    restaurant.crowd.add(a)
            for f in planning:
                magic_number = random.randint(1, 5)
                if magic_number % 2 == 0:
                    restaurant.planning.add(f)
            for r in payments:
                magic_number = random.randint(1, 20)
                if magic_number % 2 == 0:
                    restaurant.payments.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} restaurants created!"))
