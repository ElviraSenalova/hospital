# Generated by Django 5.0.3 on 2024-07-08 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_contacts_doctor_contact_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='api.doctor'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='api.patient'),
        ),
    ]
