# Generated by Django 4.2.7 on 2023-12-20 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_message_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='talk_username',
            field=models.CharField(default='.', max_length=20),
        ),
    ]