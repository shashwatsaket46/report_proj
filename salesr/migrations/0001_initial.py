# Generated by Django 5.0 on 2023-12-15 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('profiles', '0001_initial'),
        ('proudcts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='csvs')),
                ('activated', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.FloatField(blank=True)),
                ('created', models.DateTimeField(blank=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proudcts.product')),
            ],
        ),
        migrations.CreateModel(
            name='Salesr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(blank=True, max_length=12)),
                ('total_price', models.FloatField(blank=True)),
                ('created', models.DateTimeField(blank=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('positions', models.ManyToManyField(to='salesr.position')),
                ('salesman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profiles')),
            ],
        ),
    ]
