# Generated by Django 2.1.3 on 2018-11-11 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='person',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='quote',
            name='place',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]