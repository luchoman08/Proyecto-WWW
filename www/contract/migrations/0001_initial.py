# Generated by Django 3.0.3 on 2020-02-28 04:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contract_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('client_id', models.UUIDField(editable=False)),
                ('predial', models.FloatField()),
                ('address', models.CharField(max_length=30)),
                ('meter', models.UUIDField()),
                ('active', models.BooleanField()),
            ],
        ),
    ]