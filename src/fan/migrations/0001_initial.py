# Generated by Django 4.2.3 on 2023-07-09 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
                ('slug', models.SlugField(unique=True)),
                ('_direction_state', models.IntegerField(choices=[(0, 'Forward'), (1, 'Reverse')], default=0)),
                ('_speed_state', models.IntegerField(choices=[(0, 'Off'), (1, 'Slow'), (2, 'Medium'), (3, 'Fast')], default=0)),
            ],
        ),
    ]
