# Generated by Django 3.0.7 on 2021-10-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='uploads/% Y/% m/% d/')),
                ('facebook_link', models.URLField(max_length=300)),
                ('linkedin_link', models.URLField(max_length=300)),
                ('twitter_link', models.URLField(max_length=300)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
