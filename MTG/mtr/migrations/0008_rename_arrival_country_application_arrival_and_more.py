# Generated by Django 4.1.6 on 2023-05-17 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtr', '0007_application_day_alter_application_month'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='arrival_country',
            new_name='arrival',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='departure_country',
            new_name='departure',
        ),
        migrations.RemoveField(
            model_name='application',
            name='departure_city',
        ),
    ]
