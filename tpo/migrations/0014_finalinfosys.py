# Generated by Django 2.2.3 on 2019-10-20 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpo', '0013_auto_20191017_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='finalinfosys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clg_name', models.CharField(max_length=120)),
                ('count', models.CharField(max_length=40)),
            ],
        ),
    ]
