# Generated by Django 4.1.6 on 2023-05-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtr', '0011_application_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='number',
            field=models.CharField(max_length=13, verbose_name='Номер телефону'),
        ),
    ]
