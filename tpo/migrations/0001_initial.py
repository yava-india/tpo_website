# Generated by Django 2.2.3 on 2019-09-18 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A_1_Salasar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('number2', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('clg_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=40)),
                ('reporting_time', models.CharField(blank=True, max_length=50)),
                ('profile', models.CharField(blank=True, max_length=50)),
                ('confirmation', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Amazon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number2', models.BigIntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('clg_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=40)),
                ('slot', models.CharField(blank=True, max_length=15)),
                ('confirmation', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Google',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number2', models.BigIntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('clg_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=40)),
                ('slot', models.CharField(blank=True, max_length=15)),
                ('confirmation', models.CharField(blank=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Headstrait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number2', models.BigIntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('clg_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=40)),
                ('slot', models.CharField(blank=True, max_length=15)),
                ('confirmation', models.CharField(blank=True, max_length=6)),
            ],
        ),
    ]
