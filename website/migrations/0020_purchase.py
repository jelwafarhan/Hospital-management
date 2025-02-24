# Generated by Django 5.0.4 on 2024-09-21 17:54

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_alter_patient_reg_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('purchase_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.medicine')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.patient')),
            ],
        ),
    ]
