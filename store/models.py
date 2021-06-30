from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Store(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    body = models.TextField()
    body2=models.TextField()
    image = models.ImageField(upload_to="store/", blank=True, null=True)
    thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(200,300)], format = "JPEG")

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]
