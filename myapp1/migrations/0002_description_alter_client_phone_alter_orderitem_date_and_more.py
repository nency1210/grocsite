# Generated by Django 4.1.5 on 2023-02-01 17:18

import datetime
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('time', models.DateTimeField(verbose_name=datetime.datetime(2023, 2, 1, 17, 17, 47, 345533))),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('0', 'cancelled'), ('1', 'placed_order'), ('2', 'shipped_order'), ('3', 'deliverd_order')], default='1', max_length=2),
        ),
    ]