# Generated by Django 3.2.8 on 2021-11-22 14:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='invite_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
