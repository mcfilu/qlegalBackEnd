# Generated by Django 4.1.7 on 2023-02-20 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_alter_team_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='images/team/', verbose_name='picture of the team member'),
        ),
    ]
