# Generated by Django 4.2.1 on 2023-07-06 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_drugs_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugs',
            name='mfg',
            field=models.DateField(),
        ),
    ]