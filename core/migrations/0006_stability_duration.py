# Generated by Django 4.2.1 on 2023-07-06 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_drugs_batch_alter_drugs_mfg'),
    ]

    operations = [
        migrations.AddField(
            model_name='stability',
            name='duration',
            field=models.IntegerField(null=True),
        ),
    ]
