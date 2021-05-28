from rest_framework import serializers

from apps.debugtalks.models import DebugTalks


class DebugModelSerializer(serializers.ModelSerializer):
    class Meta():
        # 指定参考哪一个模型类创建
        model = DebugTalks
        # 指定为模型类的那些字段，来生成序列化器
        fields = "__all__"
