from django.db import models

# Create your models here.

from .utils import code_generator, create_shortcode


class KirrURL(models.Model):
    url       = models.CharField(max_length=200,)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated   = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)


    def save(self, *args, **kwards):
        if not self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(*args, **kwards)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)





'''
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
'''
