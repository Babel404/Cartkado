# Generated by Django 3.2 on 2021-04-09 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartkado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartkado',
            name='unique_key',
            field=models.CharField(default='-', max_length=200),
        ),
    ]