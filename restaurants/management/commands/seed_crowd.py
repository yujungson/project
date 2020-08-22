from django.core.management.base import BaseCommand
from restaurants.models import Crowd


class Command(BaseCommand):

    help = "This command creates crowd"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many crowd do you want to create")

    def handle(self, *args, **options):
        crowd = [
            "관광객",
            "단체석",
            "대학생",
            "미혼 남녀",
            "성소수자",
            "유아동반 / 가족모임에적합",
            "해외 관광객",
            "현지인",
        ]
        for f in crowd:
            Crowd.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(crowd)} crowd created!"))
