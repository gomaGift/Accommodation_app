# Generated by Django 4.2.7 on 2023-11-03 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_roomapplication_reviewed_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='identification_num',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
