# Generated by Django 2.2.3 on 2019-11-01 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpo', '0016_zycus'),
    ]

    operations = [
        migrations.CreateModel(
            name='virtusa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('clg_name', models.CharField(max_length=100)),
                ('number2', models.CharField(max_length=100)),
                ('degtype', models.CharField(max_length=15)),
                ('passyear', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=40)),
                ('confirmation', models.CharField(blank=True, max_length=6)),
            ],
        ),
    ]
