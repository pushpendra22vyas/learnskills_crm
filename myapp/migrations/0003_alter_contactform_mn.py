# Generated by Django 3.2.5 on 2021-12-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_contactform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='mn',
            field=models.CharField(max_length=256),
        ),
    ]