# Generated by Django 4.1.6 on 2023-03-09 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applytrackerapi', '0004_cover_letter_job_job_service_role_resume_reminder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='companyjobs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_per_job', to='applytrackerapi.company'),
        ),
    ]
