from django.db import models


class ProjectQuerySet(models.QuerySet):
    pass


class ProjectManager(models.Manager.from_queryset(ProjectQuerySet)):
    pass


class VersionQuerySet(models.QuerySet):
    pass


class VersionManager(models.Manager.from_queryset(VersionQuerySet)):
    pass


class TemplateQuerySet(models.QuerySet):
    pass


class TemplateManager(models.Manager.from_queryset(TemplateQuerySet)):
    pass


class DiagramQuerySet(models.QuerySet):
    pass


class DiagramManager(models.Manager.from_queryset(DiagramQuerySet)):
    pass


class RequestToReviewQuerySet(models.QuerySet):
    pass


class RequestToReviewManager(models.Manager.from_queryset(RequestToReviewQuerySet)):
    pass
