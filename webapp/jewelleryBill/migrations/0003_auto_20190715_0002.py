# Generated by Django 2.2.3 on 2019-07-14 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelleryBill', '0002_billform'),
    ]

    operations = [
        migrations.AddField(
            model_name='billform',
            name='Rate',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='billform',
            name='discount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='billform',
            name='grossWeight',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='billform',
            name='making',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='billform',
            name='netWeight',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='billform',
            name='otherChargesAmount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
