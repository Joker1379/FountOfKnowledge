from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')
	access = models.CharField(
		choices = [('standart', 'standart'),
			('moderator', 'moderator'),
			('admin', 'admin')
		],
		default = 'standart',
		max_length = 20
	)

	def __str__(self):
		return f'{self.user.username} profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)
		img = Image.open(self.image.path)
		if img.height > 150 or img.width > 150:
			output_size = (150, 150)
			img.thumbnail(output_size)
			img.save(self.image.path)
