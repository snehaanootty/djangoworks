# Generated by Django 4.1.7 on 2023-03-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('display', models.CharField(default='lcd', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('rate', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=230)),
                ('fuel_type', models.CharField(max_length=240)),
                ('kms', models.CharField(max_length=260)),
                ('number', models.CharField(max_length=230, unique=True)),
                ('description', models.CharField(max_length=2000)),
                ('owner_type', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
