from django.core.management.base import BaseCommand
from restaurants.models import Amenities


class Command(BaseCommand):

    help = "This command creates amenities"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many amenities do you want to create")

    def handle(self, *args, **options):
        amenities = [
            "남녀 공용 화장실",
            "바",
            "애완견 환영",
            "어린이 환영",
            "어린이용 높은 의자",
            "어린이용 보조 의자",
            "화장실",
        ]
        for f in amenities:
            Amenities.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(amenities)} amenities created!"))
