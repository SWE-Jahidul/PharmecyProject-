# Generated by Django 2.2.4 on 2019-08-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlpanel', '0005_auto_20190821_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mtypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='medicine',
            name='mtype',
            field=models.CharField(default='tablet', max_length=100),
        ),
    ]