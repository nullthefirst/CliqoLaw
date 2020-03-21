# Generated by Django 3.0.3 on 2020-03-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliqo', '0014_auto_20200307_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
                ('random', models.FileField(upload_to='random/')),
            ],
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='task',
        ),
    ]
