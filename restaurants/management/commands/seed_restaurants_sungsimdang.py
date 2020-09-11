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
                "name": "성심당",
                "city": "대전 중구",
                "address": "대전 중구 은행동 145",
                "description": "대전 맛집이지만 전국 방방곡곡 안오는 손님들이 없는 전국 맛집!!! 대전에서 서울까지 사가는 튀김소보로와 부추빵은 최고입니다!!!!",
                "host": lambda x: random.choice(all_users),
                "service_options": lambda x: random.choice(service_options),
                "guests": lambda x: random.randint(2, 8),
                "menu_1": "튀김소보로",
                "price_1": "1500",
                "menu_2": "부추빵",
                "price_2": "1800",
                "menu_3": "성심순크림빵",
                "price_3": "2000",
                "menu_4": "애플파이",
                "price_4": "2500",
                "menu_5": "보문산메아리",
                "price_5": "5000",
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
                    file=f"restaurant_photos/sungsimdang_{i}.jpg",
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
