# Generated by Django 3.1.1 on 2020-12-19 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20201218_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Title tag is for to be displayed instead of title', max_length=120),
        ),
    ]
