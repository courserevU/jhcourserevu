# Generated by Django 4.0.2 on 2022-03-27 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('course_num', models.CharField(max_length=20)),
                ('num_credits', models.FloatField(default=-1)),
                ('department', models.CharField(default='', max_length=255, null=True)),
                ('level', models.CharField(default='', max_length=500, null=True)),
                ('prerequisites', models.TextField(default='', null=True)),
                ('corequisites', models.TextField(default='', null=True)),
                ('school', models.CharField(db_index=True, max_length=100)),
                ('campus', models.CharField(default='', max_length=300)),
                ('is_writing_intensive', models.CharField(default='', max_length=10)),
                ('meeting_section', models.CharField(max_length=50)),
                ('size', models.IntegerField(default=-1)),
                ('enrollment', models.IntegerField(default=-1)),
                ('waitlist', models.IntegerField(default=-1)),
                ('instructors', models.CharField(default='TBD', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_updated', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.semester'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='', null=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.review')),
            ],
        ),
    ]
