# Generated by Django 4.0.4 on 2022-07-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='blog_photo'),
        ),
    ]
