# Generated by Django 4.1.4 on 2023-01-27 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='images/no_image.png', null=True, upload_to='images/'),
        ),
    ]
