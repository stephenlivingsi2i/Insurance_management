# Generated by Django 4.0.4 on 2022-05-17 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insurance',
            old_name='employee_id',
            new_name='employee',
        ),
    ]
