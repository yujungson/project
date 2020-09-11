import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from restaurants import models as restaurants_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many rooms you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        service_options = restaurants_models.ServiceOptions.objects.all()
        seeder.add_entity(
            restaurants_models.Restaurant,
            number,
            {
                "name": "단디",
                "city": "서울 송파구",
                "address": "서울 송파구 백제고분로 45길 7",
                "host": lambda x: random.choice(all_users),
                "service_options": lambda x: random.choice(service_options),
                "guests": lambda x: random.randint(2, 4),
                "description": "숯불에 구워낸 중독적인 맛과 식감의 원조 한우 대창 덮밥",
                "menu_1": "호르몬동",
                "price_1": "10500",
                "menu_2": "특호르몬동",
                "price_2": "13500",
                "menu_3": "아나고동",
                "price_3": "13000",
                "menu_4": "단디다마고",
                "price_4": "5000",
                "menu_5": "나마비루 310ml (생맥주)",
                "price_5": "2000",
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        highlights = restaurants_models.Highlights.objects.all()
        accessibilities = restaurants_models.Accessibility.objects.all()
        offerings = restaurants_models.Offerings.objects.all()
        dining_options = restaurants_models.DiningOptions.objects.all()
        amenities = restaurants_models.Amenities.objects.all()
        atmosphere = restaurants_models.Atmosphere.objects.all()
        crowd = restaurants_models.Crowd.objects.all()
        planning = restaurants_models.Planning.objects.all()
        payments = restaurants_models.Payments.objects.all()

        for pk in created_clean:
            restaurant = restaurants_models.Restaurant.objects.get(pk=pk)
            for i in range(1, 6):
                restaurants_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    restaurant=restaurant,
                    file=f"restaurant_photos/dandi_{i}.jpg",
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

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
