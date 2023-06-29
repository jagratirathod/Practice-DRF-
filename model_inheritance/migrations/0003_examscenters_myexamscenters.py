# Generated by Django 4.1.4 on 2023-04-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_inheritance', '0002_examcenter_student_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamsCenters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='MyExamsCenters',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('model_inheritance.examscenters',),
        ),
    ]
