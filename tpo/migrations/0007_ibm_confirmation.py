# Generated by Django 2.2.3 on 2019-10-05 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpo', '0006_remove_ibm_confirmation'),
    ]

    operations = [
        migrations.AddField(
            model_name='ibm',
            name='confirmation',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
