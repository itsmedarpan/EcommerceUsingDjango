from django.core.management.base import BaseCommand
from order.models import Order

class Command(BaseCommand):
    help = 'Set all existing orders to status=shipped (demo purpose)'

    def handle(self, *args, **options):
        updated = Order.objects.filter(status=Order.ORDERED).update(status=Order.SHIPPED)
        self.stdout.write(self.style.SUCCESS(f'Updated {updated} orders to shipped.'))
