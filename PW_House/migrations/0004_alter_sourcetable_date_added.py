# Generated by Django 4.0 on 2021-12-08 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PW_House', '0003_rename_sources_sourcetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcetable',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
