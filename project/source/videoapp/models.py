from django.db import models


class Video(models.Model):
    class Meta:
        db_table = 'video'
    video_id = models.CharField(max_length=200)
    video_name = models.CharField(max_length=200)
    video_views = models.IntegerField(default=0)
    video_date = models.DateTimeField('date published')

    def __str__(self):
        return self.video_name


class Comment(models.Model):
    class Meta:
        db_table = 'comment'
    comment = models.TextField()
    comment_video = models.ForeignKey(Video)

    def __str__(self):
        return self.comment_video
