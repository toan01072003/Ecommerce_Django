# Generated by Django 5.1.6 on 2025-03-31 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nation', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=20)),
                ('office_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
