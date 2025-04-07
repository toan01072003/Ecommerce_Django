# Generated by Django 5.1.6 on 2025-03-31 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shared.address')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shared.address')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shared.address')),
            ],
        ),
    ]
