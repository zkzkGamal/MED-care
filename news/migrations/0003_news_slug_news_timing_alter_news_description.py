# Generated by Django 4.1.1 on 2022-12-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='timing',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.CharField(max_length=3000),
        ),
    ]