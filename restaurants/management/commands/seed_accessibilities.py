from django.core.management.base import BaseCommand
from restaurants.models import Accessibility


class Command(BaseCommand):

    help = "This command creates accessibilities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many accessibilities do you want to create"
        )

    def handle(self, *args, **options):
        accessibilities = [
            "휠체어 이용가능 입구",
            "휠체어 이용가능 좌석",
            "휠체어 이용가능 주차장",
            "휠체어 이용가능 화장실",
        ]
        for f in accessibilities:
            Accessibility.objects.create(name=f)
        self.stdout.write(
            self.style.SUCCESS(f"{len(accessibilities)} accessibilities created!")
        )
