from django.core.management.base import BaseCommand
from rooms.models import Atmosphere


class Command(BaseCommand):

    help = "This command creates atmosphere"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many atmosphere do you want to create"
        )

    def handle(self, *args, **options):
        atmosphere = [
            "로맨틱",
            "빈티지",
            "아늑함",
            "여유로운 식사 분위기",
            "유서 깊은 장소",
            "조용한 대화",
            "조용함",
            "캐주얼",
            "캐주얼하고 소박함",
            "파티 분위기",
            "활기찬 분위기",
        ]
        for f in atmosphere:
            Atmosphere.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(atmosphere)} atmosphere created!"))
