# Generated by Django 4.2.6 on 2023-11-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='text',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
