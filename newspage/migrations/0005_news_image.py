# Generated by Django 4.2.9 on 2024-02-03 06:51

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspage', '0004_alter_comment_options_alter_news_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
