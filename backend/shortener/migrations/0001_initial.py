# Generated by Django 4.1.4 on 2022-12-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('short_id', models.SlugField(max_length=6, primary_key=True, serialize=False)),
                ('http_url', models.URLField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
