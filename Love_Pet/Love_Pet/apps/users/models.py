from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True, null=False, verbose_name="手机号")
    f_uid = models.ManyToManyField(to="User", through="Follow", through_fields=("uid", "fid"))

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'


class Follow(models.Model):
    uid = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name='a', to_field="id")
    fid = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name='b', to_field="id")

    class Meta:
        db_table = 'tb_follow'
