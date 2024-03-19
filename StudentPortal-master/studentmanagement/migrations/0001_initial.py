# Generated by Django 3.2.7 on 2021-10-03 20:08

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
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('reg_number', models.CharField(max_length=20, null=True)),
                ('phone', models.IntegerField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('course_name', models.CharField(max_length=100, null=True)),
                ('course_level', models.CharField(choices=[('Certificate', 'Certificate'), ('Diploma', 'Diploma')], max_length=200, null=True)),
                ('fee_required', models.IntegerField(null=True)),
                ('fee_paid', models.IntegerField(null=True)),
                ('fee_balance', models.IntegerField(null=True)),
                ('fee_status', models.CharField(choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=200, null=True)),
                ('cert_status', models.CharField(choices=[('Collected', 'Collected'), ('Not collected', 'Not collected')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
