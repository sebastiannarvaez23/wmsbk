# Generated by Django 4.1.6 on 2023-02-12 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('picking', '0003_rename_statuspicking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picking',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Responsable'),
        ),
    ]
