# Generated by Django 5.0.4 on 2024-09-19 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_patient_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.CharField(default=1, max_length=246),
            preserve_default=False,
        ),
    ]
