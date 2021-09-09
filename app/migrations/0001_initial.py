# Generated by Django 3.2.7 on 2021-09-09 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('capital_name', models.CharField(max_length=50)),
                ('area_name', models.IntegerField()),
            ],
        ),
    ]
