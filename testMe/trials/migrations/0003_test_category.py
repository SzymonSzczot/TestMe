# Generated by Django 3.2.9 on 2021-12-11 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trials', '0002_test_passing_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
    ]
