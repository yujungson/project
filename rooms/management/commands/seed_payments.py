from django.core.management.base import BaseCommand
from rooms.models import Payments


class Command(BaseCommand):

    help = "This command creates payments"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many payments do you want to create")

    def handle(self, *args, **options):
        payments = [
            "직불카드",
            "현금으로만결제가능",
            "NFC모바일결제",
        ]
        for f in payments:
            Payments.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(payments)} payments created!"))
