# Generated by Django 2.1.5 on 2019-02-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
