# Generated by Django 4.1.7 on 2023-02-17 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='speakers name')),
                ('surname', models.CharField(max_length=50, verbose_name='speakers surname')),
                ('description', models.TextField(verbose_name='description of the speaker')),
                ('image', models.ImageField(upload_to='', verbose_name='picture of the speaker')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='link to speakers linkedin profile')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='link speakers twitter profile')),
            ],
        ),
    ]