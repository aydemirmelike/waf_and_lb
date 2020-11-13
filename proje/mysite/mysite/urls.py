from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tez/', include('tez.urls')),
    path('admin/', admin.site.urls),
]
