from django.urls import path

from apps.projects import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

router = routers.SimpleRouter()

router.register(r'project', views.ProjectsViewSet)

urlpatterns = [
    path('login/', obtain_jwt_token)
]

urlpatterns += router.urls
