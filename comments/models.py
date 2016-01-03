from django.db import models

class Comments(models.Model):
	user_id = models.IntegerField()
	book_id = models.IntegerField()
	subject = models.TextField(max_length=255)
	body = models.TextField()
	author = models.TextField(max_length=255)
	voteup = models.IntegerField()
	votedown = models.IntegerField()
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()
	
	# python manage.py syncdb
	# python manage.py shell