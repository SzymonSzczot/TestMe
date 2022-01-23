# Generated by Django 3.2.9 on 2022-01-22 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trials', '0009_auto_20220122_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tests', to=settings.AUTH_USER_MODEL),
        ),
    ]