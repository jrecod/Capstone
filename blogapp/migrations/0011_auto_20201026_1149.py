# Generated by Django 3.1.1 on 2020-10-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_auto_20201023_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='category',
            new_name='categories',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_post_images/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='blog_category_images/'),
        ),
    ]
