# Generated by Django 5.0.4 on 2024-09-05 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='billingadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=246)),
                ('bio', models.CharField(max_length=246)),
            ],
        ),
        migrations.CreateModel(
            name='hadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=246)),
                ('bio', models.CharField(max_length=246)),
            ],
        ),
    ]
