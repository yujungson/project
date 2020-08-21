import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=50, type=int, help="How many rooms you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        service_options = room_models.ServiceOptions.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "service_options": lambda x: random.choice(service_options),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        highlights = room_models.Highlights.objects.all()
        accessibilities = room_models.Accessibility.objects.all()
        offerings = room_models.Offerings.objects.all()
        dining_options = room_models.DiningOptions.objects.all()
        amenities = room_models.Amenities.objects.all()
        atmosphere = room_models.Atmosphere.objects.all()
        crowd = room_models.Crowd.objects.all()
        planning = room_models.Planning.objects.all()
        payments = room_models.Payments.objects.all()

        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 20)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
            for a in highlights:
                magic_number = random.randint(1, 20)
                if magic_number % 2 == 0:
                    room.highlights.add(a)
            for f in accessibilities:
                magic_number = random.randint(1, 5)
                if magic_number % 2 == 0:
                    room.accessibilities.add(f)
            for r in offerings:
                magic_number = random.randint(1, 20)
                if magic_number % 2 == 0:
                    room.offerings.add(r)

            for a in dining_options:
                magic_number = random.randint(1, 20)
                if magic_number % 2 == 0:
                    room.dining_options.add(a)
            for f in amenities:
                magic_number = random.randint(1, 5)
                if magic_number % 2 == 0:
                    room.amenities.add(f)
            for r in atmosphere:
                magic_number = random.randint(1, 20)
                if magic_number % 2 == 0:
                    room.atmosphere.add(r)
            for a in crowd:
                magic_number = random.randint(1, 20)
                if magic_number % 2 == 0:
                    room.crowd.add(a)
            for f in planning:
                magic_number = random.randint(1, 5)
                if magic_number % 2 == 0:
                    room.planning.add(f)
            for r in payments:
                magic_number = random.randint(1, 20)
                if magic_number % 2 == 0:
                    room.payments.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
