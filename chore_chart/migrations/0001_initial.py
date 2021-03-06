# Generated by Django 2.1.7 on 2019-07-21 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chore_name', models.CharField(max_length=264, unique=True)),
                ('description', models.CharField(max_length=264, null=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=4)),
                ('image', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.CharField(choices=[('monster', 'Monster'), ('princess', 'Princess'), ('unicorn', 'Unicorn'), ('dinosaur', 'Dinosaur'), ('car', 'Car')], default='princess', max_length=10)),
                ('bank', models.IntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
