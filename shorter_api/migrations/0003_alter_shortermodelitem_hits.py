# Generated by Django 4.2.5 on 2023-09-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorter_api', '0002_shortermodelitem_delete_shortermodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortermodelitem',
            name='hits',
            field=models.PositiveIntegerField(),
        ),
    ]
