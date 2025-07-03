import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Furniture_shop.settings')
django.setup()

from product.models import Product
from django.db import transaction

def fix_duplicate_slugs():
    seen = set()
    with transaction.atomic():
        for product in Product.objects.all().order_by('id'):
            original_slug = product.slug
            n = 1
            while product.slug in seen or Product.objects.filter(slug=product.slug).exclude(pk=product.pk).exists():
                product.slug = f"{original_slug}-{n}"
                n += 1
            seen.add(product.slug)
            product.save()
    print('Duplicate slugs fixed.')

if __name__ == "__main__":
    fix_duplicate_slugs()
