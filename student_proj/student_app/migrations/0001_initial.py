# Generated by Django 5.1 on 2024-08-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=15)),
                ('std', models.CharField(max_length=10)),
            ],
        ),
    ]
