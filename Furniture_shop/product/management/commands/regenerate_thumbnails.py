from django.core.management.base import BaseCommand
from product.models import Product

class Command(BaseCommand):
    help = 'Regenerate all product thumbnails.'

    def handle(self, *args, **options):
        count = 0
        for product in Product.objects.all():
            if product.image:
                print(f'Regenerating thumbnail for: {product.name}')
                product.thumbnail = product.make_thumbnail(product.image)
                product.save()
                count += 1
        self.stdout.write(self.style.SUCCESS(f'Regenerated thumbnails for {count} products.'))
