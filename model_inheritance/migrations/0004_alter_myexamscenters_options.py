# Generated by Django 4.1.4 on 2023-04-20 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_inheritance', '0003_examscenters_myexamscenters'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myexamscenters',
            options={'ordering': ['id']},
        ),
    ]
