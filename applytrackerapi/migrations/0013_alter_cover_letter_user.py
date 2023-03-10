# Generated by Django 4.1.6 on 2023-03-10 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applytrackerapi', '0012_resume_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cover_letter',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
