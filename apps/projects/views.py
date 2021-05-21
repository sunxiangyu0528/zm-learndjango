from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from apps.projects.models import Projects
from apps.projects.serializer import ProjectModelSerializer, \
    ProjectNameSerializer, InterfaceByProjectIdSerializer


# ViewSet不再支持get，post，put等请求方法，只支持action动作
class ProjectsViewSet(viewsets.ModelViewSet):
    """
    项目视图
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    # ordering_fields = ['name', 'leader']
    # filterset_fields = ['name', 'leader']
    # action装饰器来声明自定义的动作
    # methods参数用于指定该动作支持的请求方式，默认为get
    # 默认实例方法名就是动作名
    @action(methods=['GET'], detail=False, url_path='nm', url_name='url_names')
    def names(self, request):
        project = self.get_queryset()
        serializer = ProjectNameSerializer(instance=project, many=True)
        # return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    # 获取项目id为1的所有接口
    @action(detail=True)
    def interfaces(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = InterfaceByProjectIdSerializer(instance=instance)
        return Response(serializer.data)
