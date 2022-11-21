from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300:
            output_size = (300, int(300/img.height*img.width))
        if img.width > 300:
            output_size = (int(300/img.height*img.width), 300)
        if img.width > 300 or img.height > 300:
            img = img.resize(output_size)
            img.save(self.image.path)

