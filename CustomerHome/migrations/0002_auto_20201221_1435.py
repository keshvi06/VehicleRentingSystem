# Generated by Django 3.0.4 on 2020-12-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerHome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_city',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_country',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_pincode',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_state',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_age',
            field=models.IntegerField(),
        ),
    ]
