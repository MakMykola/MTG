# Generated by Django 4.1.6 on 2023-05-17 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtr', '0006_application_arrival_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='day',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')], default='', max_length=50, verbose_name='День:'),
        ),
        migrations.AlterField(
            model_name='application',
            name='month',
            field=models.CharField(choices=[('1', 'Січень'), ('2', 'Лютий'), ('3', 'Березень'), ('4', 'Квітень'), ('5', 'Травень'), ('6', 'Червень'), ('7', 'Липень'), ('8', 'Серпень'), ('9', 'Вересень'), ('10', 'Жовтень'), ('11', 'Листопад'), ('12', 'Грудень')], max_length=50, verbose_name='Місяць:'),
        ),
    ]
