from django.db import models

# Create your models here.
from utils.base_models import BaseModel


class DebugTalks(BaseModel):
    id = models.AutoField(verbose_name="id主键", primary_key=True, help_text="id主键")
    name = models.CharField(verbose_name="debugtalk名称", max_length=200, help_text="debugtalk名称")
    debugtalk = models.TextField(null=True, default='#debugtalk.py', help_text='debugtalk文件')
    project = models.OneToOneField('projects.Projects', on_delete=models.CASCADE, related_name='debugtalks',
                                   help_text='所属项目')

    class Meta:
        db_table = 'tb_debugtalks'
        verbose_name = 'debugtalks.py文件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
