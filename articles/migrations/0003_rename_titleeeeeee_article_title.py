# Generated by Django 4.2.7 on 2023-11-07 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_title_article_titleeeeeee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='titleeeeeee',
            new_name='title',
        ),
    ]
