from django.db import models


class Numeral(models.Model):
    num_value = models.CharField(max_length=255)
    num_type = models.CharField(max_length=255)
    parent_textarea_id = models.CharField(max_length=255)
