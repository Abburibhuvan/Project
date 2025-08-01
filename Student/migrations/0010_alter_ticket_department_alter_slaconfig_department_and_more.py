# Generated by Django 5.2.1 on 2025-06-07 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0009_department_sla_hours_ticket_slabreachlog_and_more'),
        ('core', '0009_department_sla_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.department'),
        ),
        migrations.AlterField(
            model_name='slaconfig',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.department'),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
