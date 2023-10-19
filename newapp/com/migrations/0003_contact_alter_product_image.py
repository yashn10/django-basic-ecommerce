# Generated by Django 4.2.4 on 2023-08-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com', '0002_product_category_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=10)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(default=''),
        ),
    ]
