from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from studentmanagement.models import Student


def student_profile(sender, instance, created, **kwargs):
    if created:
        group, created = Group.objects.get_or_create(name='student')
        instance.groups.add(group)

        Student.objects.create(
            user=instance,
            full_name=instance.username,
            email = instance.email
        )

post_save.connect(student_profile, sender= User)