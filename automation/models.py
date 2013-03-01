from django.forms import ModelForm
from django.db import models

class UploadFile(models.Model):
    ip=models.CharField(max_length=50)
    ifile=models.FileField(upload_to="upload/tmp/")
    created=models.DateTimeField(auto_now=True)

class UploadFileForm(ModelForm):
    class Meta:
        model=UploadFile

class generateMedia(models.Model):
	PRODUCT_LIST=(
			('Inventor','Inventor'),
			('FDSADV','FDSADV'),
			('Naviswork','Naviswork'),
			('Vault','Vault'),
	)
	MEDIA_TYPE=(
			('ALL','ALL'),
			('COMMON','COMMON'),
			('DLM','DLM'),
			('WI','WI'),
			('IMG','IMG'),
			('ISO','ISO'),
	)
	LAN_LIST=(
			('ENU','ENU'),
			('DEU','DEU'),
			('FRA','FRA'),
			('JPN','JPN'),
			('CHS','CHS'),
			('CHT','CHT'),
			('PLK','PLK'),
	)
	product=models.CharField(max_length=100,choices=PRODUCT_LIST)
	language=models.CharField(max_length=100,choices=LAN_LIST)
	mediatype=models.CharField(max_length=100,choices=MEDIA_TYPE)
	created=models.DateTimeField(auto_now=True)

class generateMediaForm(ModelForm):
	class Meta:
		model=generateMedia
