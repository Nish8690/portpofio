# Generated by Django 2.2.11 on 2020-07-23 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200723_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='comments',
            new_name='proj_desc',
        ),
        migrations.RemoveField(
            model_name='project',
            name='file',
        ),
        migrations.RemoveField(
            model_name='project',
            name='proj_id',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='proj_file',
            field=models.FileField(default=None, upload_to='pf/images'),
        ),
        migrations.AddField(
            model_name='project',
            name='proj_image',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='pub_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='project',
            name='sub_category',
            field=models.CharField(default='', max_length=50),
        ),
    ]
