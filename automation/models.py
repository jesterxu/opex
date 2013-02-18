from django.forms import ModelForm
from django.db import models

class UploadFile(models.Model):
    ip=models.CharField(max_length=50)
    ifile=models.FileField(upload_to="upload/tmp/")
    created=models.DateTimeField(auto_now=True)


class UploadFileForm(ModelForm):
    class Meta:
        model=UploadFile
