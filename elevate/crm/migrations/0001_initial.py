# Generated by Django 5.0.1 on 2024-02-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mb_no', models.IntegerField(max_length=10)),
                ('register_no', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('pasout', models.FloatField()),
            ],
        ),
    ]