# Generated by Django 4.0.2 on 2022-03-27 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jhed_id', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('jhed_email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('class_year', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('preferred_name', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('is_admin', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
