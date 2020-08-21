from django.core.management.base import BaseCommand
from rooms.models import Planning


class Command(BaseCommand):

    help = "This command creates planning"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many planning do you want to create")

    def handle(self, *args, **options):
        planning = [
            "브런치 예약을 권장함",
            "점심식사 예약을 권장함",
            "저녁식사 예약을 권장함",
            "예약을 권장함",
            "일반적으로 대기 시간이 있음",
            "트랜스젠더 안전 구역",
            "LGBTQ 환영",
        ]
        for f in planning:
            Planning.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(planning)} planning created!"))
