# Generated by Django 4.2.7 on 2023-12-11 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_teacherprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='education',
            field=models.TextField(),
        ),
    ]