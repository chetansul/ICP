# Generated by Django 4.2.1 on 2023-07-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_result_humidity_alter_result_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugs',
            name='packmaterial',
            field=models.CharField(max_length=158, verbose_name='Package Material'),
        ),
    ]
