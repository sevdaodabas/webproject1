# Generated by Django 5.1.7 on 2025-04-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passport_type',
            name='image',
            field=models.URLField(default='https://flagcdn.com/w320/default.png', max_length=500),
            preserve_default=False,
        ),
    ]
