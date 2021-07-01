# Generated by Django 3.2 on 2021-07-01 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('body2', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='store/')),
            ],
        ),
        migrations.CreateModel(
            name='Store2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('body2', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='store/')),
            ],
        ),
    ]
