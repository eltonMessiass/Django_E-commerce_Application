# Generated by Django 5.0.6 on 2024-07-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0002_customeruser_delete_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='customer_users', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='customer_users', to='auth.permission'),
        ),
    ]
