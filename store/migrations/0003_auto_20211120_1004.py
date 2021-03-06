# Generated by Django 3.2.9 on 2021-11-20 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_products_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stock_count', models.IntegerField(help_text='How many items are currently in stock')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(default='')),
                ('sku', models.CharField(default='', max_length=20, unique=True, verbose_name='Stock Keeping Unit')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
