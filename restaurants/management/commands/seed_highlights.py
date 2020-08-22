from django.core.management.base import BaseCommand
from restaurants.models import Highlights


class Command(BaseCommand):

    help = "This command creates many highlights"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many highlights do you want to create"
        )

    def handle(self, *args, **options):
        highlights = [
            "다양한 맥주",
            "다양한 발효술",
            "다양한 수제맥주",
            "다양한 와인",
            "다양한 차",
            "라이브 공연",
            "라이브 음악",
            "멋진 라이브 음악",
            "멋진 전망",
            "벽난로",
            "비공개 이벤트",
            "스포츠 경기 관람",
            "신속한 서비스",
            "야외 좌석",
            "옥상 좌석",
            "우수한 가치",
            "유명한 지역 대표 음식메뉴",
            "좋은 건강식 메뉴",
            "풍미있는 커피",
            "훌륭한 디저트",
        ]
        for a in highlights:
            Highlights.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Highlights created!"))
