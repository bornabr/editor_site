# Generated by Django 2.1.5 on 2019-02-07 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0004_auto_20190203_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_share',
            field=models.BooleanField(default=False),
        ),
    ]