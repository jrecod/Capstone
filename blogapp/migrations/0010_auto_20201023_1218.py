# Generated by Django 3.1.1 on 2020-10-23 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_auto_20201022_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
