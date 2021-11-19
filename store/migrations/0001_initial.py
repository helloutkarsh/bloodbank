# Generated by Django 3.2.9 on 2021-11-17 21:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=75)),
                ('mobile_number', models.IntegerField()),
                ('city', models.CharField(max_length=75)),
                ('pincode', models.CharField(max_length=6)),
                ('documentId', models.PositiveIntegerField()),
            ],
        ),
    ]