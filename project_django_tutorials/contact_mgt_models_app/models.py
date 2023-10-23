from django.db import models

# Create your models here.

def user_directory_path(instance, filename): 

	# file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
	return 'user_{0}/{1}'.format(instance.id, filename) 


class Contact(models.Model):
	upload = models.ImageField(upload_to = user_directory_path)
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	email = models.EmailField(max_length = 254)
	address = models.TextField()
	age = models.IntegerField()
	birth_date = models.DateField()
 
