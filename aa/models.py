from django.db import models

class Process(models.Model):
    upload = models.ImageField(upload_to="data_dump")
    result = models.ImageField(upload_to="data_dump", blank=True, null=True)
    processed = models.BooleanField(default=False, blank=True)
    
    class Meta:
        verbose_name="Process"
