# Generated by Django 3.2.16 on 2022-11-21 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blearn_app', '0005_content_new_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='new_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
