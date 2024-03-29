# Generated by Django 4.1.6 on 2023-03-15 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applytrackerapi', '0019_remove_company_job_company_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='job',
        ),
        migrations.RemoveField(
            model_name='job',
            name='companyjobs',
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_company', to='applytrackerapi.company'),
        ),
        migrations.CreateModel(
            name='InterviewAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_interviews', to='applytrackerapi.contact')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interview_name', to='applytrackerapi.interview')),
            ],
        ),
    ]
