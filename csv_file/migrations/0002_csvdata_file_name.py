# Generated by Django 3.0.8 on 2020-08-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_file', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvdata',
            name='file_name',
            field=models.CharField(default='test.csv', max_length=255),
        ),
    ]
