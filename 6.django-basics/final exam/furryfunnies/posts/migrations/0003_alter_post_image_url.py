# Generated by Django 5.1.2 on 2024-10-27 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.URLField(help_text='Share your funniest furry photo URL!'),
        ),
    ]
