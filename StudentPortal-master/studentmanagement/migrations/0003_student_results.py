# Generated by Django 3.2.7 on 2021-10-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanagement', '0002_alter_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='results',
            field=models.CharField(choices=[('Passed', 'Passed'), ('Failed', 'Failed'), ('Referral', 'Referral')], max_length=100, null=True),
        ),
    ]