from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    # 유저 모델을 참조하는 경우
    # 방법1. (권장하지 않음)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 방법2. (권장) settings.AUTH_USER_MODEL == 'accounts.User'
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 방법3. (권장)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)