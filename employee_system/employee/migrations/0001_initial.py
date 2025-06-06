# Generated by Django 5.1.7 on 2025-04-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='ชื่อ')),
                ('last_name', models.CharField(max_length=100, verbose_name='นามสกุล')),
                ('position', models.CharField(max_length=100, verbose_name='ตำแหน่ง')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='เงินเดือน')),
                ('phone_number', models.CharField(max_length=15, verbose_name='เบอร์โทร')),
            ],
        ),
    ]
