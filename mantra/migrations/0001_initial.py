# Generated by Django 4.2.4 on 2023-08-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mantra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1000, verbose_name='Name of Mantra')),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Banner Image')),
                ('exact_mantra', models.TextField(blank=True, null=True, verbose_name='Exact Mantra')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description meaning of Mantra')),
                ('link', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Link of audio file')),
                ('loop_count', models.IntegerField(default=0, verbose_name='Loop Count of Mantra')),
                ('views_count', models.IntegerField(default=0, verbose_name='Views Count of Mantra')),
            ],
            options={
                'verbose_name_plural': 'Mantras',
            },
        ),
    ]