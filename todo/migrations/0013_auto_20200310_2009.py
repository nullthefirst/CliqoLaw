# Generated by Django 3.0.3 on 2020-03-10 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_auto_20200310_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='ref',
        ),
        migrations.AddField(
            model_name='task',
            name='reference_number',
            field=models.CharField(default='#REF0000', max_length=100, unique=True),
        ),
    ]
