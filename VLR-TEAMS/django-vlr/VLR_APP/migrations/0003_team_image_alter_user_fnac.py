# Generated by Django 4.1.3 on 2022-12-18 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VLR_APP', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fnac',
            field=models.DateField(),
        ),
    ]
