from django.db import models
#from .utils import TopGenerator


class BestVideo(models.Model):
    video_id = models.CharField(max_length=1000, help_text='url')
    video_name = models.CharField(max_length=200, help_text='name video')
    views_number = models.CharField(max_length=10, help_text='position in raiting')
    pub_date = models.DateTimeField('date published')

    def save(self, *args, **kwargs):
        #self.best = TopGenerator()
        super(BestVideo, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.video_name)
