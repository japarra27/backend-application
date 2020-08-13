# Generated by Django 3.1 on 2020-08-13 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200813_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crearevento',
            name='event_address',
            field=models.CharField(max_length=128, verbose_name='Dirección del evento'),
        ),
        migrations.AlterField(
            model_name='crearevento',
            name='event_category',
            field=models.CharField(choices=[(1, 'Conferencia'), (2, 'Seminario'), (3, 'Congreso'), (4, 'Curso')], max_length=16, verbose_name='Categoría del evento'),
        ),
        migrations.AlterField(
            model_name='crearevento',
            name='event_name',
            field=models.CharField(max_length=128, verbose_name='Nombre del evento'),
        ),
        migrations.AlterField(
            model_name='crearevento',
            name='event_place',
            field=models.CharField(max_length=128, verbose_name='Lugar del evento'),
        ),
        migrations.AlterField(
            model_name='crearevento',
            name='event_type',
            field=models.CharField(choices=[(1, 'Virtual'), (2, 'Presencial')], max_length=10, verbose_name='Modalidad del evento'),
        ),
        migrations.AlterField(
            model_name='crearevento',
            name='thumbnail',
            field=models.ImageField(default='recipe_thumbnails/default.png', upload_to='recipe_thumbnails', verbose_name='Imagen'),
        ),
    ]
