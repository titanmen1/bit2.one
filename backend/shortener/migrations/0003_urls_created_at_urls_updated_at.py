# Generated by Django 4.1.4 on 2022-12-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_remove_urls_count_remove_urls_http_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='urls',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
