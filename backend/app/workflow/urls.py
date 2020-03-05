from django.urls import path, include

from workflow import views

from rest_framework import routers


router = routers.DefaultRouter()
router.register('workflow', views.WorkflowView)

app_name = 'workflow'

urlpatterns = [
    path('', include(router.urls)),
]
