from django.db import models

from osp.models.abstract_timestamp import AbstractTimestamp
from osp.utils import question_types

class Question(AbstractTimestamp):

    label = models.CharField(max_length=255)
    data_type = models.CharField(
        max_length=8,
        choices=question_types.DATA_TYPES,
        default='char'
    )
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField()
    required = models.BooleanField(default=False)