# Generated by Django 3.0.5 on 2020-04-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20200424_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]