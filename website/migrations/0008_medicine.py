# Generated by Django 5.0.4 on 2024-09-06 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_rename_bio_billingadmin_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=246)),
                ('use', models.CharField(max_length=246)),
                ('price', models.CharField(max_length=246)),
            ],
        ),
    ]
