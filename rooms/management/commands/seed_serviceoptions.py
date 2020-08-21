from django.core.management.base import BaseCommand
from rooms.models import ServiceOptions


class Command(BaseCommand):

    help = "This command creates serviceoptions"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many service options do you want to create"
        )

    def handle(self, *args, **options):
        serviceoptions = [
            "테이크 아웃",
            "배달 서비스",
            "매장 서비스",
            "매장 밖 수령",
            "매장 내 식사",
            "드라이브스루 매장",
        ]
        for f in serviceoptions:
            ServiceOptions.objects.create(name=f)
        self.stdout.write(
            self.style.SUCCESS(f"{len(serviceoptions)} serviceoptions created!")
        )
