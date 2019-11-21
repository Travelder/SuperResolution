# Generated by Django 2.2.5 on 2019-11-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(upload_to='data_dump')),
                ('result', models.ImageField(blank=True, null=True, upload_to='data_dump')),
                ('processed', models.BooleanField(blank=True, default=False)),
            ],
            options={
                'verbose_name': 'Process',
            },
        ),
    ]
