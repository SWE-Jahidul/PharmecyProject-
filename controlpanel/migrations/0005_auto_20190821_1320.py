# Generated by Django 2.2.4 on 2019-08-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlpanel', '0004_auto_20190723_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='quantity',
        ),
        migrations.AddField(
            model_name='medicine',
            name='generic',
            field=models.CharField(default='', max_length=100),
        ),
    ]
