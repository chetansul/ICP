# Generated by Django 4.2.1 on 2023-07-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_company_drugs_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugs',
            name='expirydate',
            field=models.DateField(null=True, verbose_name='Expiry Date'),
        ),
        migrations.AlterField(
            model_name='drugs',
            name='mfg',
            field=models.DateField(null=True, verbose_name='Manufacture Date'),
        ),
    ]