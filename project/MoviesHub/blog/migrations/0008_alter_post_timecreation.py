# Generated by Django 4.1.7 on 2023-03-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timeCreation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
