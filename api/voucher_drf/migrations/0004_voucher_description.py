# Generated by Django 3.1.1 on 2020-09-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher_drf', '0003_remove_voucher_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='description',
            field=models.CharField(default='0% Off', max_length=15),
        ),
    ]