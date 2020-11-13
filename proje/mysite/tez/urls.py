from django.urls import path,include
from django.conf.urls import url,include

from . import views

urlpatterns = [
    path('', include('django_sb_admin.urls'))
]
