from django.db import models
from django.contrib.auth import get_user_model

# app 만들었을땐 무조건 config -> settings.py -> INSTALLED_APPS 에 추가해야한다!

User = get_user_model()

# verbose_name : 필드에대한 이름 지정 -> 표기해줘도되고 안해줘도됨


class Post(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    writer = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, blank=True)


class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE)
    writer = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, blank=True)
