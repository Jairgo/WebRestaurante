# Generated by Django 3.2.7 on 2021-10-05 14:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 5, 14, 45, 11, 196581, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]