# Generated by Django 3.2.8 on 2021-10-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]