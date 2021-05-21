from django.db import models


class BaseModel(models.Model):
    """
    数据库公用表字段
    """
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除', help_text='逻辑删除')

    class Meta:
        abstract = True
        verbose_name = '公共字段表'
        db_table = 'BaseModel'


