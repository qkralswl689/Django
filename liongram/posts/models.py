from email.mime import image
from django.db import models

# app 만들었을땐 무조건 config -> settings.py -> INSTALLED_APPS 에 추가해야한다!


class Post(models.Model):
    # verbose_name : 필드에대한 이름 지정 -> 표기해줘도되고 안해줘도됨
    image = models.ImageField(verbose_name='이미지')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField('작성일')
    view_count = models.IntegerField('조회수')
