# Generated by Django 3.2.5 on 2021-12-15 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher_detailes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='teachers_profiles/%Y/%m/%d')),
                ('subject', models.CharField(blank=True, max_length=256, null=True)),
                ('dob', models.CharField(blank=True, max_length=256, null=True)),
                ('city', models.CharField(blank=True, max_length=256, null=True)),
                ('contect_number', models.CharField(blank=True, max_length=256, null=True)),
                ('gender', models.CharField(blank=True, max_length=256, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]