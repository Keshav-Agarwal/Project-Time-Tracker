# Generated by Django 3.1 on 2020-08-10 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeentry',
            name='description',
            field=models.TextField(default='something', max_length=100),
        ),
    ]