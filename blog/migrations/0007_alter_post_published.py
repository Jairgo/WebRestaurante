# Generated by Django 3.2.7 on 2021-10-14 00:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 14, 0, 43, 9, 458597, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]