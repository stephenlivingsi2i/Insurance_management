# Generated by Django 4.0.4 on 2022-05-18 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('contact_number', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField()),
            ],
        ),
    ]