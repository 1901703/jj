from django.db import models
from config import settings


class Post(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    post_title=models.CharField(max_length=50)
    post_image=models.ImageField(upload_to="", blank=True, null=True)
    contents=models.TextField()
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    top_fixed = models.BooleanField(verbose_name='상단고정', default=False)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.post_title

class Comment(models.Model):
    comment=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
