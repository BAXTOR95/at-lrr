from django.urls import path, include

from upload import views

from rest_framework import routers


router = routers.DefaultRouter()
router.register('file', views.FileUploadView)

app_name = 'upload'

urlpatterns = [
    path('', include(router.urls)),
]
