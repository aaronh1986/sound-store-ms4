# Generated by Django 3.2.8 on 2021-10-27 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogcomments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcomments',
            options={'verbose_name_plural': 'Blog Comments'},
        ),
    ]
