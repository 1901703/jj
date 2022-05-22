# Generated by Django 3.1.5 on 2022-05-22 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20220521_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
                ('item_image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('meta_description', models.TextField(blank=True)),
                ('item_price', models.IntegerField(verbose_name='상품가격')),
                ('item_amt', models.PositiveIntegerField()),
                ('available_display', models.BooleanField(default=True, verbose_name='Display')),
                ('available_order', models.BooleanField(default=True, verbose_name='Order')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='shop.category')),
            ],
            options={
                'ordering': ['-created'],
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]