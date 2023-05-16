from django.db import models


class ReviewChoices(models.IntegerChoices):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
