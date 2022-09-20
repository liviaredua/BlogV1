# Generated by Django 4.1 on 2022-09-20 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_profile_slug_profile_hello'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='emailProfile',
            field=models.EmailField(default=1, max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='locate',
            field=models.CharField(default=1, max_length=150, verbose_name='Locate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default=1, max_length=20, verbose_name='Phone'),
            preserve_default=False,
        ),
    ]
