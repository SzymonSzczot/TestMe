# Generated by Django 3.2.9 on 2021-12-11 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reset_code',
            field=models.IntegerField(),
        ),
    ]
