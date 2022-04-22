# Generated by Django 4.0.2 on 2022-04-22 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0004_comment_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.ManyToManyField(to='course.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
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
