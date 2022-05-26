# Generated by Django 2.1 on 2022-05-26 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pName', models.CharField(max_length=255)),
                ('pPrice', models.FloatField()),
                ('pStock', models.IntegerField()),
                ('pImage_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
