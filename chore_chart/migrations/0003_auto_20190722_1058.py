# Generated by Django 2.1.7 on 2019-07-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chore_chart', '0002_userprofileinfo_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='bank',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='goal',
            field=models.IntegerField(default=0),
        ),
    ]