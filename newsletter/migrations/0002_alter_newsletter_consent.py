# Generated by Django 3.2 on 2022-05-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='consent',
            field=models.BooleanField(default=False),
        ),
    ]
