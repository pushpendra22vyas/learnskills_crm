# Generated by Django 3.2.5 on 2021-12-18 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_contactform_mn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='lnane',
            new_name='lname',
        ),
    ]
