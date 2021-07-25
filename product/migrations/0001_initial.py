# Generated by Django 3.2.5 on 2021-07-24 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.basemodel')),
                ('name', models.CharField(help_text='Name of product.', max_length=256)),
                ('unit', models.PositiveIntegerField(default=1, help_text='Amount of available products. default 1')),
                ('short_description', models.TextField(blank=True, default='', help_text='Short summary, can be used in search results.')),
                ('long_description', models.TextField(blank=True, default='', help_text='Long Description')),
                ('weight', models.DecimalField(blank=True, decimal_places=3, help_text='Default weight of product. On variant level weight can be entered per product.', max_digits=13, null=True)),
                ('release_date', models.DateField(blank=True, help_text='Release date. Product release on date, can be used for taking pre-orders.', null=True)),
                ('pre_order', models.BooleanField(default=False, help_text='Can be pre ordered', verbose_name='Product is a pre-order product')),
                ('is_serviceable', models.BooleanField(default=False, help_text='Is the product serviceable')),
                ('valid_from', models.DateTimeField(blank=True, help_text='Enter the datetime from which the product is valid', null=True, verbose_name='Valid from')),
                ('valid_until', models.DateTimeField(blank=True, help_text="Enter the datetime on which the product's validity expires", null=True, verbose_name='Valid until')),
                ('image_thumbnail', models.ImageField(blank=True, help_text='Use this for the thumbnail', max_length=500, null=True, upload_to='product_images/%Y/%m/%d/', verbose_name='Thumbnail image')),
                ('image_alternative_1', models.ImageField(blank=True, help_text='Additional image', max_length=500, null=True, upload_to='product_images/%Y/%m/%d/', verbose_name='Alternative image 1')),
                ('image_alternative_2', models.ImageField(blank=True, help_text='Additional image', max_length=500, null=True, upload_to='product_images/%Y/%m/%d/', verbose_name='Alternative image 2')),
                ('image_alternative_3', models.ImageField(blank=True, help_text='Additional image', max_length=500, null=True, upload_to='product_images/%Y/%m/%d/', verbose_name='Alternative image 3')),
                ('image_alternative_4', models.ImageField(blank=True, help_text='Additional image', max_length=500, null=True, upload_to='product_images/%Y/%m/%d/', verbose_name='Alternative image 4')),
            ],
            options={
                'ordering': ['-id', 'name'],
            },
            bases=('common.basemodel',),
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.basemodel')),
                ('name', models.CharField(help_text='Name of the Brand', max_length=128, unique=True)),
                ('description', models.TextField(help_text='Small Description of the Brand')),
                ('is_available', models.BooleanField(default=True, help_text='Brand is available or not')),
            ],
            options={
                'ordering': ['-id', 'name'],
            },
            bases=('common.basemodel',),
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.basemodel')),
                ('color_name', models.CharField(help_text='Color Name.', max_length=128, verbose_name='Color Name')),
                ('color_code', models.CharField(choices=[('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'), ('black', 'Black'), ('white', 'White'), ('orange', 'Orange'), ('yellow', 'Yellow')], help_text='Color Code.', max_length=128, unique=True, verbose_name='Color Code')),
                ('is_available', models.BooleanField(default=True, help_text='color is available or not')),
            ],
            options={
                'ordering': ['-id', 'color_code'],
            },
            bases=('common.basemodel',),
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.basemodel')),
                ('name', models.CharField(help_text='Name of the Option Group', max_length=128, unique=True)),
                ('description', models.TextField(help_text='Description of the Group')),
                ('is_available', models.BooleanField(default=True, help_text='Brand is available or not')),
            ],
            options={
                'ordering': ['-id', 'name'],
            },
            bases=('common.basemodel',),
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.basemodel')),
                ('name', models.CharField(help_text='Name of the Option Group', max_length=128, unique=True)),
                ('description', models.TextField(help_text='Description of the Option Group')),
                ('is_available', models.BooleanField(default=True, help_text='Brand is available or not')),
            ],
            options={
                'ordering': ['-id', 'name'],
            },
            bases=('common.basemodel',),
        ),
        migrations.AddIndex(
            model_name='producttype',
            index=models.Index(fields=['name', 'is_available'], name='product_pro_name_50175e_idx'),
        ),
        migrations.AddIndex(
            model_name='productgroup',
            index=models.Index(fields=['name', 'is_available'], name='product_pro_name_6699b1_idx'),
        ),
        migrations.AddIndex(
            model_name='productcolor',
            index=models.Index(fields=['color_code', 'is_available'], name='product_pro_color_c_323504_idx'),
        ),
        migrations.AddIndex(
            model_name='productbrand',
            index=models.Index(fields=['name', 'is_available'], name='product_pro_name_c72138_idx'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, help_text='related product brand', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.productbrand'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_group',
            field=models.ForeignKey(blank=True, help_text='related product group.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.productgroup'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(blank=True, help_text='related product type', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.producttype'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name', 'product_group', 'product_type', 'brand', 'unit'], name='product_pro_name_79e569_idx'),
        ),
    ]
