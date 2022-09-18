from django.conf.urls import include, url
from . import views

app_name = 'cad'

urlpatterns = [
	url(r'^upload_csv/$', views.upload_csv, name='cad_upload_csv'),
]