from django.db import models

from .choices import ReviewChoices
from .managers import ProjectManager, VersionManager, TemplateManager, DiagramManager, RequestToReviewManager


class Organization(models.Model):
    name = models.CharField(max_length=100)


class Project(models.Model):
    """
    because we have to have ability to create new version, project object cant hold any data.
    """
    name = models.CharField(max_length=100)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    objects = ProjectManager()


class Version(models.Model):
    """
    each project should have at least one version.
    first version is created automatically, when project is created.
    """
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    major = models.PositiveSmallIntegerField()
    minor = models.PositiveSmallIntegerField()
    patch = models.PositiveSmallIntegerField()
    objects = VersionManager()

    def __str__(self):
        return f'{self.major}.{self.minor}.{self.patch}'


class Template(models.Model):
    """
    sample model for templates
    """
    name = models.CharField(max_length=100)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    version = models.ForeignKey('Version', on_delete=models.CASCADE)
    objects = TemplateManager()

    @property
    def project(self):
        """
        to remove some code duplication, we can use this property
        :return:
        """
        return self.version.project


class Diagram(models.Model):
    """
    sample model for diagrams
    """
    name = models.CharField(max_length=100)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    version = models.ForeignKey('Version', on_delete=models.CASCADE)
    objects = DiagramManager()

    @property
    def project(self):
        return self.version.project


class RequestToReview(models.Model):
    """
    each time, when a project is updated, a new request to review is created.
    each request to review has a status, when it is accepted, we can create new version.
    after that, we have to clone all templates and diagrams from the previous version.
    because client needs to have archived version of templates and diagrams.
    """
    name = models.CharField(max_length=100)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=ReviewChoices.choices)
    objects = RequestToReviewManager()


class ReviewAccess(models.Model):
    """
    this is special access model, which is created for each request to review.
    clients want to have ability to set this access per reviewer.
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    request_to_review = models.ForeignKey('RequestToReview', on_delete=models.CASCADE)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


class ReviewComment(models.Model):
    """
    this is part of next feature, which is not implemented yet.
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    access = models.ForeignKey('ReviewAccess', on_delete=models.CASCADE)
    comment = models.TextField()
