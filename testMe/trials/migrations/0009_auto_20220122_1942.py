# Generated by Django 3.2.9 on 2022-01-22 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trials', '0008_auto_20220122_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solvedtest',
            name='test',
        ),
        migrations.AddField(
            model_name='solvedtest',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='trials.test'),
        ),
        migrations.RemoveField(
            model_name='solvedtest',
            name='user',
        ),
        migrations.AddField(
            model_name='solvedtest',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL),
        ),
    ]
