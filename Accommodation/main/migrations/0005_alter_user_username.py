# Generated by Django 4.2.7 on 2023-11-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_user_email_alter_user_identification_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
