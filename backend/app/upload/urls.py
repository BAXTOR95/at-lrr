from django.urls import path

from upload import views


app_name = 'user'

urlpatterns = [
    path('', views.FileUploadView.as_view()),
]
