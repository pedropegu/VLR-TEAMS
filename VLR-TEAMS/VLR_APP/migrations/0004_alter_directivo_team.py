# Generated by Django 4.1.3 on 2023-01-08 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VLR_APP', '0003_alter_directivo_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directivo',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='VLR_APP.team'),
        ),
    ]
