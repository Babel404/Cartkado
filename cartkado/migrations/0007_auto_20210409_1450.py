# Generated by Django 3.2 on 2021-04-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartkado', '0006_auto_20210409_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartkado',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]