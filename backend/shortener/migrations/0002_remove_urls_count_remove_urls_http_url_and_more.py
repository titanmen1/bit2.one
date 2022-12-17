# Generated by Django 4.1.4 on 2022-12-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urls',
            name='count',
        ),
        migrations.RemoveField(
            model_name='urls',
            name='http_url',
        ),
        migrations.RemoveField(
            model_name='urls',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='urls',
            name='short_id',
        ),
        migrations.AddField(
            model_name='urls',
            name='full_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='urls',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='urls',
            name='short_url',
            field=models.URLField(null=True),
        ),
    ]