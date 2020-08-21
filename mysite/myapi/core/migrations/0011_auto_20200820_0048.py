# Generated by Django 3.1 on 2020-08-20 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200814_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crearevento',
            name='event_type',
            field=models.CharField(choices=[('Virtual', 'Virtual'), ('Presencial', 'Presencial')], max_length=16, verbose_name='Modalidad del evento'),
        ),
    ]
