# Generated by Django 3.0.2 on 2020-03-04 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliqo', '0009_auto_20200304_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newmatter',
            name='contact_address',
        ),
        migrations.RemoveField(
            model_name='newmatter',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='newmatter',
            name='contact_name',
        ),
        migrations.RemoveField(
            model_name='newmatter',
            name='contact_phone',
        ),
        migrations.AlterField(
            model_name='collaboratorinfo',
            name='ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliqo.NewMatter', to_field='reference_number', verbose_name='Reference Number'),
        ),
        migrations.AlterField(
            model_name='newmatter',
            name='client_name',
            field=models.CharField(default='Client Name', max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliqo.NewMatter', to_field='reference_number', verbose_name='Reference Number'),
        ),
        migrations.CreateModel(
            name='NewContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(default='Contact Name', max_length=250)),
                ('contact_phone', models.CharField(default='+27123456789', max_length=20)),
                ('contact_email', models.EmailField(default='contact@domain.com', max_length=254)),
                ('contact_address', models.TextField(default='Contact Address')),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliqo.NewMatter', to_field='reference_number', verbose_name='Reference Number')),
            ],
        ),
        migrations.CreateModel(
            name='NewClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_phone', models.CharField(default='+27123456789', max_length=20)),
                ('client_email', models.EmailField(default='client@domain.com', max_length=254)),
                ('client_address', models.TextField(default='Client Address')),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliqo.NewMatter', to_field='reference_number', verbose_name='Reference Number')),
            ],
        ),
    ]
