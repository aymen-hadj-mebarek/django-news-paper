# Generated by Django 5.1.2 on 2024-10-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='parent',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
