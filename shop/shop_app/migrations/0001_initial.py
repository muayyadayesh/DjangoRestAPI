# Generated by Django 3.2.6 on 2021-09-11 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=256)),
                ('product_price', models.FloatField()),
                ('product_quantity', models.PositiveIntegerField()),
            ],
        ),
    ]
