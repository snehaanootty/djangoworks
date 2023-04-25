# Generated by Django 4.1.7 on 2023-03-18 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('flavour', models.CharField(max_length=200)),
                ('shape', models.CharField(max_length=200)),
                ('layer', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('weight', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
