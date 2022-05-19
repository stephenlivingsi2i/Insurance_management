# Generated by Django 4.0.4 on 2022-05-19 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('policy', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_number', models.CharField(max_length=15)),
                ('uhid', models.BigIntegerField()),
                ('insurance_name', models.CharField(max_length=50)),
                ('insurance_type', models.CharField(max_length=50)),
                ('insurance_amount', models.IntegerField()),
                ('start_date', models.DateField()),
                ('renewal_date', models.DateField()),
                ('issued_by', models.CharField(max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('policy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='policy.policy')),
            ],
        ),
    ]
