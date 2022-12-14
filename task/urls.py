"""
URL mappings for the profile app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from task import views


router = DefaultRouter()
router.register('tasks', views.TaskViewSet)
router.register('tasks_alls', views.TaskAllViewSet)

app_name = 'task'

urlpatterns = [
    path('', include(router.urls)),
]
