# Generated by Django 3.0.3 on 2020-03-10 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_auto_20200310_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='ref',
        ),
    ]