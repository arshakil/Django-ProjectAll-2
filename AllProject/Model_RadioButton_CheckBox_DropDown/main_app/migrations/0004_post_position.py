# Generated by Django 2.2.5 on 2019-09-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_post_media_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='position',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
