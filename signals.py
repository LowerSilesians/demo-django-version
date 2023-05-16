# method for updating
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Project, Version


@receiver(post_save, sender=Project)
def create_version(sender, instance, created: bool, **kwargs):
    if created:
        Version.objects.create(
            major=1,
            minor=0,
            patch=0,
            project=instance,
            organization=instance.organization,
        )
