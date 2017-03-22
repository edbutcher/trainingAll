from django.db import models
#from .utils import TopGenerator
# Create your models here.


class BestVideo(models.Model):
    best = models.CharField(max_length=1000, help_text='url')
    name_video = models.CharField(max_length=200, help_text='name video')
    number_in = models.CharField(max_length=10, help_text='position in raiting')
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        #self.best = TopGenerator()
        super(BestVideo, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name_video)
