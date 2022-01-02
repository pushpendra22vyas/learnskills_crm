# Generated by Django 3.2.5 on 2021-12-18 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('photo', models.FileField(blank=True, null=True, upload_to='Gallary/%Y/%m/%d')),
                ('catagory', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
