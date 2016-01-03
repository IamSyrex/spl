from django.db import models

# Create your models here.
class Books(models.Model):
	title = models.TextField(max_length=255)
	subtitle = models.TextField(max_length=255)
	description = models.TextField()
	published_date = models.DateField()
	pages = models.IntegerField()
	slug = models.TextField()
	
	# python manage.py syncdb
	# python manage.py shell