# Generated by Django 3.0.5 on 2020-04-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_article_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_heading',
            field=models.TextField(default=''),
        ),
    ]