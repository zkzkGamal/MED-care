# Generated by Django 4.1.1 on 2022-12-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_doctor_email_recption'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='coverimg',
            field=models.ImageField(blank=True, null=True, upload_to='phote'),
        ),
    ]
