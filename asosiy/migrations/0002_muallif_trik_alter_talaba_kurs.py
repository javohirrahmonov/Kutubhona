# Generated by Django 4.2 on 2023-04-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='muallif',
            name='trik',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='talaba',
            name='kurs',
            field=models.SmallIntegerField(default=3),
        ),
    ]
