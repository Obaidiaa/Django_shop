from django.db import models

# models created with this base will inherit created_date and modified_date automatically
class DatesBaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True