# Generated by Django 4.1.6 on 2023-03-09 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applytrackerapi', '0009_alter_job_applied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='interviewer_email',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='interviewer_name',
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=155)),
                ('last_name', models.CharField(max_length=155)),
                ('email', models.CharField(max_length=155, null=True)),
                ('linkedin_url', models.CharField(max_length=155, null=True)),
                ('title', models.CharField(max_length=155, null=True)),
                ('phone', models.CharField(max_length=155, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_company', to='applytrackerapi.company')),
            ],
        ),
        migrations.AddField(
            model_name='interview',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interview_contact', to='applytrackerapi.contact'),
        ),
        migrations.AddField(
            model_name='job',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_contact', to='applytrackerapi.contact'),
        ),
    ]
