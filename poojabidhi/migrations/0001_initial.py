# Generated by Django 4.2.4 on 2023-08-16 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PoojaBidhi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1000, verbose_name='Name of Pooja Bidhi')),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Banner Image')),
                ('exact_poojabidhi', models.TextField(blank=True, null=True, verbose_name='Exact Pooja Bidhi')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description meaning of Pooja Bidhi')),
                ('link', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Link of audio file')),
                ('loop_count', models.IntegerField(default=0, verbose_name='Loop Count of Pooja Bidhi')),
                ('views_count', models.IntegerField(default=0, verbose_name='Views Count of Pooja Bidhi')),
            ],
            options={
                'verbose_name_plural': 'Pooja Bidhis',
            },
        ),
    ]
