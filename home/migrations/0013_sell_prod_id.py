# Generated by Django 3.2.7 on 2021-11-03 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_fibuy_prod_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='prod_id',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
