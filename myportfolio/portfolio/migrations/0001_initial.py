# Generated by Django 2.2.11 on 2020-07-20 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_id', models.IntegerField()),
                ('proj_name', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=400)),
            ],
        ),
    ]