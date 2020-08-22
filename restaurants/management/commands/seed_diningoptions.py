from django.core.management.base import BaseCommand
from restaurants.models import DiningOptions


class Command(BaseCommand):

    help = "This command creates diningoptions"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many dining options do you want to create"
        )

    def handle(self, *args, **options):
        diningoptions = [
            "아침식사",
            "브런치",
            "점심식사",
            "저녁식사",
            "케이터링",
            "디저트",
            "미리주문",
            "좌석",
            "테이블주문서비스",
        ]
        for f in diningoptions:
            DiningOptions.objects.create(name=f)
        self.stdout.write(
            self.style.SUCCESS(f"{len(diningoptions)} diningoptions created!")
        )
