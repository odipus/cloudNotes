from django.db import models

# Create your models here.
class UploadFile(models.Model):
    file_name = models.FileField(upload_to='./uploadFile')
    uploader = models.CharField(max_length=32)
    upload_time = models.DateField()
