# Generated by Django 4.2.2 on 2023-06-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('items', models.TextField()),
                ('lat_long', models.CharField(max_length=100)),
                ('full_details', models.TextField()),
            ],
        ),
    ]