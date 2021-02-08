# Generated by Django 3.1 on 2021-01-20 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=64)),
                ('Password', models.CharField(max_length=128)),
                ('Role', models.CharField(max_length=64)),
                ('Email', models.EmailField(max_length=254)),
                ('Wallet', models.FloatField()),
                ('Owed', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('BikeId', models.AutoField(primary_key=True, serialize=False)),
                ('BikeState', models.BooleanField()),
                ('BikeType', models.CharField(max_length=64)),
                ('Location', models.CharField(max_length=128)),
                ('Condition', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderId', models.AutoField(primary_key=True, serialize=False)),
                ('BikeId', models.IntegerField()),
                ('UserId', models.IntegerField()),
                ('StartLocation', models.CharField(max_length=128)),
                ('EndLocation', models.CharField(max_length=128)),
                ('StartTime', models.DateTimeField(auto_now_add=True)),
                ('EndTime', models.DateTimeField()),
                ('Bill', models.FloatField()),
                ('OrderState', models.BooleanField()),
            ],
        ),
    ]
