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
                "name": "콰이어트 크림티",
                "city": "서울 송파구",
                "address": "서울 송파구 삼전로12길 7",
                "host": lambda x: random.choice(all_users),
                "service_options": lambda x: random.choice(service_options),
                "guests": lambda x: random.randint(2, 4),
                "description": "스콘과 클로티드 크림, 잼과 함께 즐길 수 있는 곳",
                "menu_1": "달콤한 오리지널 밀크티",
                "price_1": "7500",
                "menu_2": "캐러멜 루이보스 밀크티",
                "price_2": "8000",
                "menu_3": "홍차+스콘+클로티드 크림+ 잼",
                "price_3": "10000",
                "menu_4": "오리지널 스콘",
                "price_4": "3500",
                "menu_5": "얼그레이 스콘",
                "price_5": "3800",
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
                    file=f"restaurant_photos/quiet_{i}.jpg",
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
