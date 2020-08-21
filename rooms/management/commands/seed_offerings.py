from django.core.management.base import BaseCommand
from rooms.models import Offerings


class Command(BaseCommand):

    help = "This command creates many offerings"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many offerings do you want to create")

    def handle(self, *args, **options):
        offerings = [
            "현지 식재료",
            "커피",
            "칵테일",
            "채식 메뉴",
            "주류 제공",
            "유기농 음식",
            "와인",
            "어린이 메뉴",
            "양주",
            "심야 시간대 음식",
            "스몰 플레이트 메뉴",
            "수제 맥주",
            "무글루텐 메뉴",
            "맥주",
            "뜨거운 차",
            "고급 칵테일",
            "건강에 좋은 음식 메뉴",
        ]
        for a in offerings:
            Offerings.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Offerings created!"))
