from django.forms import ModelForm
from django.db import models
import datetime

class UploadFile(models.Model):
	MEDIA_TYPE=(
			('ISO','ISO'),
			('USB','USB'),
			('DLM','DLM'),
			('WI','WI'),
			('LP','LP'),
			)
	TASK_TYPE=(
			('Fill Release Score','Fill Release Score'),
			('Fill Vault Build Tracker','Fill Vault Build Tracker'),
			('Fill PDS Build Tracker','Fill PDS Build Tracker'),
			('Fill FDS Build Tracker','Fill FDS Build Tracker')
	)
	ip=models.CharField(max_length=50)
	mediatype=models.CharField(max_length=100,choices=MEDIA_TYPE)
	#tasktype=models.CharField(max_length=100,choices=TASK_TYPE)
	ifile=models.FileField(upload_to="upload/tmp/")
	created=models.DateTimeField(auto_now=True)
	
	def save(self, *args, **kwargs):
		self.created = datetime.datetime.now()
		super(UploadFile, self).save(*args, **kwargs)

class UploadFileForm(ModelForm):
    class Meta:
        model=UploadFile

class generateMedia(models.Model):
	PRODUCT_LIST=(
			('FDSADV','FDSADV'),
			('FDSPRM','FDSPRM'),
			('FDSSTD','FDSSTD'),
			#('Vault','Vault'),
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
			#('ENU','ENU'),
			('DEU','DEU'),
			('FRA','FRA'),
			('JPN','JPN'),
			('CHS','CHS'),
			('CHT','CHT'),
			('ESP','ESP'),
			('ITA','ITA'),
			('KOR','KOR'),
			('PLK','PLK'),
			('PTB','PTB'),
			('RUS','RUS')
	)
	product=models.CharField(max_length=100,choices=PRODUCT_LIST)
	language=models.CharField(max_length=100,choices=LAN_LIST)
	mediatype=models.CharField(max_length=100,choices=MEDIA_TYPE)
	created=models.DateTimeField(auto_now=True)

class generateMediaForm(ModelForm):
	class Meta:
		model=generateMedia
