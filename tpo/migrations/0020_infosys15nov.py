# Generated by Django 2.2.3 on 2019-11-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpo', '0019_lti12result'),
    ]

    operations = [
        migrations.CreateModel(
            name='infosys15nov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=60)),
                ('lastname', models.CharField(blank=True, max_length=60)),
                ('number2', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('clg_name', models.CharField(blank=True, max_length=100)),
                ('branch', models.CharField(blank=True, max_length=40)),
                ('confirmation', models.CharField(blank=True, max_length=6)),
            ],
        ),
    ]
