# Generated by Django 5.1.5 on 2025-01-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0002_users_color_alter_users_email_alter_users_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='userId',
        ),
        migrations.AddField(
            model_name='tasks',
            name='users',
            field=models.ManyToManyField(related_name='tasks', to='backend_app.users'),
        ),
    ]
