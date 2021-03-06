# Generated by Django 3.2.3 on 2021-06-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=250)),
                ('text', models.TextField(max_length=5000)),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Accomplishments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='pictures')),
                ('title', models.CharField(max_length=100)),
                ('paragraph', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'AccompLishment',
                'verbose_name_plural': 'AccemptLishments',
            },
        ),
    ]
