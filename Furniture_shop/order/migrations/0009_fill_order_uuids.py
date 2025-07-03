from django.db import migrations
import uuid

def fill_order_uuids(apps, schema_editor):
    Order = apps.get_model('order', 'Order')
    for order in Order.objects.filter(order_uuid__isnull=True):
        order.order_uuid = uuid.uuid4()
        order.save(update_fields=['order_uuid'])

class Migration(migrations.Migration):
    dependencies = [
        ('order', '0008_alter_order_status'),
    ]
    operations = [
        migrations.RunPython(fill_order_uuids, reverse_code=migrations.RunPython.noop),
    ]
